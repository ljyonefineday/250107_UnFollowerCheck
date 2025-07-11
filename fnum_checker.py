import requests as rq
from bs4 import BeautifulSoup
import re
import convert_to_num as cn


def get_followers(id):    
    ### connect to the website
    url = "https://www.instagram.com/" + id + "/"
    response = rq.get(url)

    ## check if the connection is successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        meta_content = soup.find('meta', attrs={'name': 'description'})

        ## cleaning the content
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', meta_content['content'])
        print(cleaned_text)

    else:
        print("웹사이트에 접속할 수 없습니다.")

    ## get followers and following numbers
    ii = 0
    followers = ''
    while cleaned_text[ii] != 'F':
        followers += cleaned_text[ii]
        ii += 1
    # print(followers)

    ii += 9
    followings = ''
    while cleaned_text[ii] != 'F':
        followings += cleaned_text[ii]
        ii += 1
    # print(followings)


    ## transform M, K, B to numbers
    followers = cn.cnumf(followers)
    followings = cn.cnumf(followings)

    return followers, followings