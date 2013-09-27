from pydelicious import get_popular, get_userposts, get_urlposts

def initializeUserDict(tag, count = 5):
  user_dict ={}
  
  # get the top "count" popular posts
  for popular_post in get_popular(tag = tag)[0: count]:
    # find all users who posted this
    for post_of_popular_url in get_urlposts(popular_post['url']):
      user = post_of_popular_url['user']
      if user != '':
        user_dict[user] = {}
  
  return user_dict

import time
def fillItems(user_dict):
  all_items = {}
  
  # Find links posted by all users
  for user in user_dict:
    for i in range(3):
      try:
        posts = get_userposts(user)
        break
      except:
        print "Failed user "+ user +", retrying"
        time.sleep(4)
    
    for post in posts:
      url = post['url']
      user_dict[user][url] = 1.0
      all_items[url] = 1
  
  # Fill in missing items with 0
  for ratings in user_dict.values( ):
    for item in all_items:
      if item not in ratings:
        ratings[item] = 0.0

