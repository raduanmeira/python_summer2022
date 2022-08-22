################################################################################
#
# Raduan van Velthem Meira
# Python summer course 2022 -- Homework 3
# August 22, 2022
#
################################################################################

# Libraries and imports 

import importlib
import os
import tweepy
import time

# os.chdir('C:\\users\\radua\\onedrive\\washu\\classes\\python_course')

twitter = importlib.import_module('start_twitter')
api = twitter.client
limit = api.rate_limit_status()

# Getting the washu account

wustl = api.get_user(screen_name = '@WUSTLPoliSci')

followers = wustl.follower_ids()

following = api.get_friend_ids(screen_name = '@WUSTLPoliSci')

### One degree of separation

# Generating empty dictionaries to fill with the necessary info

most_actives = {}
most_actives_layman = {}
most_actives_expert = {}
most_actives_celebrity = {}

most_followers = {}
most_followers_following = {}

# Followers

for i in followers:
  try:
    follower = f"{api.get_user(user_id = i)}"
    most_actives[f"{follower.screen_name}"] = follower.statuses_count
    most_followers[f"{follower.screen_name}"] = follower.followers_count
  except:
    print("sleeping")
    time.sleep(15*60)


most_actives_result = max(most_actives, key=most_actives.get)
most_followers_result = max(most_followers, key=most_followers.get)

# Following

for i, account in enumerate(following):
  try:
    most_followers_following[f'{account.screeen_name}'] = account.followers_count
    if account.followers_count < 100:
      most_actives_layman[f"{account.screen_name}"] = account.statuses_count
    if follower.followers_count < 1000:
      most_actives_expert[f"{account.screen_name}"] = account.statuses_count
    else: most_actives_celebrity[f"{account.screen_name}"] = account.statuses_count
  except:
    print("sleeping")
    time.sleep(15*60)

most_actives_layman_result = max(most_actives_layman, key=most_actives_layman.get)
most_actives_expert_result = max(most_actives_expert, key=most_actives_expert.get)
most_actives_celebrity_result = max(most_actives_celebrity, key=most_actives_celebrity.get)
most_followers_following_result = max(most_followers_following, key=most_followers_following.get)

# Final results 

print("One degree of separation")

print(
  '''
  Among the followers of @WUSTLPoliSci who is the most active?
  ''')

print(f'Answer : most_actives1')

print('''
Among the followers of @WUSTLPoliSci who is the most popular, i.e. has
the greatest number of followers?''')

print(f'Answer : {most_followers1}')

print('''
Among the friends of @WUSTLPoliSci, i.e. the users she is following, who
#are the most active layman, expert and celebrity?
#''')

print(f'''
answer:\n
layman -- {most_actives_layman_result}\n
expert -- {most_actives_expert_result}\n
celebrity -- {most_actives_celebrity_result}
''')

print('''
Among the friends of @WUSTLPoliSci who is the most popular?
''')

print(f"Answer: {most_followers_following_result}")

### Two degrees of separation

most_active_2nd = {}

for i, account in enumarate(followers):
  try:
    if account.followers_count < 1000:
      most_active_2nd[f"{account.screen_name}"] = account.statuses_count
      followers_2nd = account.followers_ids()
      for i, j in enumarate(followers_2nd):
        try:
          account_2nd = f"{api.get_user(j)}"
          most_active_2nd[f"{account_2nd.screen_name}"] = account_2nd.statuses_count
        except:
          print("sleeping")
          time.sleep(15*60)
  except:
    print("sleeping")
    time.sleep(15*60)
      
most_active_2nd_result = max(most_active_2nd, key=most_active_2nd.get)

most_active_2nd = {}

for i, account in enumarate(following):
  try:
    if account.followers_count < 1000:
      most_active_2nd[f"{account.screen_name}"] = account.statuses_count
      followers_2nd = account.followers_ids()
      for i, j in enumarate(followers_2nd):
        try:
          account_2nd = f"{api.get_user(j)}"
          most_active_2nd[f"{account_2nd.screen_name}"] = account_2nd.statuses_count
        except:
          print("sleeping")
          time.sleep(15*60)
  except:
    print("sleeping")
    time.sleep(15*60)
      
most_active_2nd_result1 = max(most_active_2nd, key=most_active_2nd.get)

# Final results

print("Two degrees of separation:")

print('''
Among the followers of @WUSTLPoliSci and their followers, who is the
most active?
''')

print(f"Answer: {most_active_2nd_result}")

print('''
Among the friends of @WUSTLPoliSci and their friends, who is the most
active?
''')

print(f"Answer: {most_active_2nd_result1}")
