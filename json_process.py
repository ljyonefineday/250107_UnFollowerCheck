import json

# laod data
followers_raw = json.load(open('data/followers.json'))
following_raw = json.load(open('data/following.json'))
# reset list
followers = []
followings = []

# processing followers
cnt_followers = 0
for temp in followers_raw:
    #print(temp['string_list_data'][0]['value'])
    followers.append(temp['string_list_data'][0]['value'])
    cnt_followers += 1

# processing followings
cnt_followings = 0
for temp in following_raw['relationships_following']:
    #print(temp['string_list_data'][0]['value'])
    followings.append(temp['string_list_data'][0]['value'])
    cnt_followings += 1

## print(followers)
## print(followings)

## print('followers = ', cnt_followers)
## print('followings = ', cnt_followings)
## print("end")

# substracting followers from followings
unfollowers = list(set(followings) - set(followers))

## print(unfollowers)
## print('Unfollowers = ',unfollowers.__len__())