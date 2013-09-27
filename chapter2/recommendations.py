# A dictionary of movie critics and their ratings of a small 
# set of movies 
critics ={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane': 4.5,'You, Me and Dupree': 1.0,'Superman Returns': 4.0}}

from math import sqrt

def shared_items_of(prefs, person1, person2):
  shared_items = {}
  for item in prefs[person1]:
    if item in prefs[person2]:
      shared_items[item] = 1

  return shared_items

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
  shared_items = shared_items_of(prefs, person1, person2)

  # if they have no ratings in common, return 0
  if len(shared_items) == 0:
    return 0

  # Add up the squares of all the differences
  sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in shared_items])
  
  return 1/(1 + sqrt(sum_of_squares))

# Returns the Pearson correlation coefficient for p1 and p2
# Source: http://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson
def sim_pearson(prefs, p1, p2):
  shared_items = shared_items_of(prefs, p1, p2)
  
  # Find the number of elements
  n = len(shared_items)
  
  # if they have no ratings in common, return 0
  if n == 0:
    return 0

  # Find means:
  p1_mean = sum([prefs[p1][item] for item in shared_items]) / n
  p2_mean = sum([prefs[p2][item] for item in shared_items]) / n

  # Find covariance:
  cov = sum([(prefs[p1][item] - p1_mean) * (prefs[p2][item] - p2_mean) for item in shared_items])

  # Find variances:
  p1_var = sum([pow(prefs[p1][item] - p1_mean, 2) for item in shared_items])
  p2_var = sum([pow(prefs[p2][item] - p2_mean, 2) for item in shared_items])

  # Pearson's coefficient:
  sd_p1_sd_p2 = sqrt(p1_var * p2_var)
  if sd_p1_sd_p2 == 0: return 0
  return cov / sd_p1_sd_p2

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs, person, n = 5, similarity = sim_pearson):
  scores = [(similarity(prefs, person, other_person), other_person) for other_person in prefs if other_person != person]
  
  # Sort the list so the highest scores appear at the top
  scores.sort()
  scores.reverse()
  return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other_person user's rankings
def getRecommendations(prefs, person, similarity = sim_pearson):
  totals = {}
  similarity_sum = {}
  
  for other_person in prefs:
    # don't compare me to myself
    if other_person == person: continue
    
    other_persons_similarity = similarity(prefs, person, other_person)
    
    # ignore scores of zero or lower
    if other_persons_similarity <= 0: continue
    
    for item in prefs[other_person]:
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item] == 0:
        # Similarity * Score 
        totals.setdefault(item, 0) 
        totals[item] += prefs[other_person][item] * other_persons_similarity
        
        # Sum of similarities
        similarity_sum.setdefault(item, 0)
        similarity_sum[item] += other_persons_similarity

  # Create the normalized list
  rankings = [(total / similarity_sum[item], item) for item, total in totals.items()]
  
  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

def transformPrefs(prefs):
  transformedPrefs = {}

  for person in prefs:
    for item in prefs[person]:
      transformedPrefs.setdefault(item, {})

      # Flip item and person
      transformedPrefs[item][person] = prefs[person][item]

  return transformedPrefs


def calculateSimilarItems(prefs, n=10):
  '''
  Create a dictionary of items showing which other items they are
  most similar to.
  '''

  result = {}

  # Invert the preference matrix to be item-centric
  itemPrefs = transformPrefs(prefs)
  c = 0
  for item in itemPrefs:
    # Status updates for large datasets
    c += 1
    if c % 100 == 0:
      print '%d / %d' % (c, len(itemPrefs))
    # Find the most similar items to this one
    scores = topMatches(itemPrefs, item, n=n, similarity=sim_distance)
    result[item] = scores

  return result

def getRecommendedItems(prefs, itemMatch, user):
  userRatings = prefs[user]
  scores = {}
  totalSim = {}
  # Loop over items rated by this user
  for (item, rating) in userRatings.items():
        # Loop over items similar to this one
            for (similarity, item2) in itemMatch[item]:
              # Ignore if this user has already rated this item
              if item2 in userRatings:
                  continue

              # Weighted sum of rating times similarity
              scores.setdefault(item2, 0)
              scores[item2] += similarity * rating

              # Sum of all the similarities
              totalSim.setdefault(item2, 0)
              totalSim[item2] += similarity

  # Divide each total score by total weighting to get an average
  rankings = [(score / totalSim[item], item) for (item, score) in
                      scores.items()]

  # Return the rankings from highest to lowest
  rankings.sort()
  rankings.reverse()
  return rankings

def loadMovieLens(path='/data/movielens'):
  # Get movie titles
  movies = {}
  for line in open(path + '/u.item'):
    (id, title) = line.split('|')[0:2]
    movies[id] = title
  # Load data
  prefs = {}
  for line in open(path + '/u.data'):
    (user, movieid, rating, ts) = line.split('\t')
    prefs.setdefault(user, {})
    prefs[user][movies[movieid]] = float(rating)
  return prefs
