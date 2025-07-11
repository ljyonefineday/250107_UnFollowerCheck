# JSON READ
import json_process as jp
import fnum_checker as fc
import time
import random

##############################################################
# Reset list
##############################################################
idff = {}

## run json_process module
jp
jp.unfollowers

# get followres and followings numbers
urltest = jp.unfollowers[0:4]
for i in urltest:
    delay = random.randint(1, 10)
    time.sleep(delay)
    #print(fc.get_followers(i))
    idff[i] = fc.get_followers(i)

print(idff)
prirnt("Followers numbers fetched successfully.")