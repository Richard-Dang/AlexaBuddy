#!/usr/bin/env python

import praw
import webbrowser
import re
import indicoio
indicoio.config.api_key = 'f813d87aeb7c1fec9b38a95f466c414f'


user_agent = "AlexaBuddy 1.0 by /u/alexabuddy"
r = praw.Reddit(user_agent=user_agent)

def authenticate ():
    r.set_oauth_app_info(client_id='FP4sj6FgPVoWZA',\
                         client_secret='7j_TQb_M2tRTICl-nXvgUkTobLA',\
                         redirect_uri='http://127.0.0.1:65010/authorize_callback')
    url = r.get_authorize_url('uniqueKey','identity read submit',True)
    webbrowser.open(url)
    access_information = r.get_access_information('mCk1x5yJphyEVJxsabth1joOvjY')
    r.set_access_credentials(**access_information)
    r.refresh_access_information(access_information['refresh_token'])
    return r

def get_top_posts(subreddit, num_posts):
    posts = []
    submissions = r.get_subreddit(subreddit).get_top(limit=num_posts)
    for  x in submissions:
        title = re.search('(?<=::).*',str(x))
        posts.append(title.group(0))
    return posts

#-------------------------------

# accepts a list
# returns a dictonary
def gradeMultiple(inputList):
    "Call this function when multiple lines need to be checked"

    # dictonary with numLines number of elements that will contain the marks of all the lines in order of appearance in inputList
    posts = []
    pos_posts = []
    neg_posts = []
    xCount = 0
    yCount = 0

    # for loop that will get the marks of all elements in inputList (assume inputList is a list of strings)
    for i in inputList:
        if indicoio.sentiment(i) > 0.5:
            pos_posts.append(i)
        else:
            neg_posts.append(i)

    posts.append(pos_posts)
    posts.append(neg_posts)

    return_posts = []

    for x in posts:
        return_posts.append([])
        for y in x:
            yCount = yCount + 1
            y = (str(yCount) + " " + y)
            return_posts[xCount].append(y)
        xCount = xCount + 1

    return return_posts

#------------------------------


# top_news_posts = get_top_posts('news',20)
# sentiment_dict = gradeMultiple(top_news_posts)
# pos_sentiment = sentiment_dict[0]
# neg_sentiment = sentiment_dict[1]
