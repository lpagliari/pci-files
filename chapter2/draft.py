import recommendations
reload(recommendations)

# Finds distances for all critics:
distances = []

for p1 in critics: 
  for p2 in critics:
    if p1 != p2:
      distances.append((recommendations.sim_distance(recommendations.critics, p1, p2), p1, p2))

distances.sort()
distances.reverse()
distances

###########################
reload(recommendations)
recommendations.sim_distance(recommendations.critics, 'Lisa Rose','Gene Seymour')
recommendations.sim_pearson(recommendations.critics, 'Lisa Rose','Gene Seymour')
recommendations.topMatches(recommendations.critics,'Toby', n = 3)

######################################################
# del.icio.us:
######################################################
delusers = deliciousrec.initializeUserDict('gratis')
delusers['lpagliari'] = {} # Add yourself to the dictionary if you use delicious
deliciousrec.fillItems(delusers)
delusers

###########################
# pick random user and find users similar to him/her:
import recommendations
reload(recommendations)
import random

user = delusers.keys()[random.randint(0, len(delusers) - 1)]
user
recommendations.topMatches(delusers, user)

###########################
# get recommendations for a user:
recommendations.getRecommendations(delusers, user)[0: 10]

reload(recommendations)
itemsim = recommendations.calculateSimilarItems(recommendations.critics)
itemsim

recommendations.getRecommendedItems(recommendations.critics, itemsim, 'Toby')

prefs = recommendations.loadMovieLens()
prefs['87']

recommendations.getRecommendations(prefs,'87')[0: 30]
