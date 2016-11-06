import praw
import webbrowser
import re
import indicoio
indicoio.config.api_key = 'f813d87aeb7c1fec9b38a95f466c414f'

user_agent = "AlexaBuddy 1.0 by /u/alexabuddy"
r = praw.Reddit(user_agent=user_agent)

#-------------------------------------

def authenticate ():
    r.set_oauth_app_info(client_id='FP4sj6FgPVoWZA',\
                         client_secret='7j_TQb_M2tRTICl-nXvgUkTobLA',\
                         redirect_uri='http://127.0.0.1:65010/authorize_callback')
    url = r.get_authorize_url('uniqueKey','identity read submit',True)
    webbrowser.open(url)
    access_information = r.get_access_information('PmyTPEiJOXZcf7IgCs1SJupYRCQ')
    r.set_access_credentials(**access_information)
    r.refresh_access_information(access_information['refresh_token'])
    return r

#-----------------------------------

def get_top_posts(subreddit, num_posts):
    posts = []
    submissions = r.get_subreddit(subreddit).get_top(limit=num_posts)
    for x in submissions:
        title = re.search('(?<=::).*',str(x))
        posts.append(title.group(0))

    return posts

#------------------------------

def get_top_posts_top_comments(subreddit, num_posts):
    comments = []
    submissions = r.get_subreddit(subreddit).get_top(limit=num_posts)
    for x in submissions:
        comments.append(x.comments[0].body)

    return comments

#-------------------------------

# accepts a list
# returns a dictonary
def gradeMultiple(inputList):
    "Call this function when multiple lines need to be checked"

    # dictonary with numLines number of elements that will contain the marks of all the lines in order of appearance in inputList
    posts = []
    pos_posts = []
    neg_posts = []

    # for loop that will get the marks of all elements in inputList (assume inputList is a list of strings)
    for i in inputList:
        if indicoio.sentiment(i) > 0.5:
            pos_posts.append(i)
        else:
            neg_posts.append(i)
    posts.append(pos_posts)
    posts.append(neg_posts)

    return posts

#------------------------------

# code used for testing here:

# top_news_posts = get_top_posts('space',3)
# sentiment_dict = gradeMultiple(top_news_posts)
# pos_sentiment = sentiment_dict[0]
# neg_sentiment = sentiment_dict[1]
#
# top_news_posts_comments = get_top_posts_top_comments('space',3)
# comments_sentiment_dict = gradeMultiple(top_news_posts_comments)
# comments_pos_sentiment = comments_sentiment_dict[0]
# comments_neg_sentiment = comments_sentiment_dict[1]

# print (pos_sentiment)
# print (neg_sentiment)
# print ("")
# print (comments_pos_sentiment)
# print (comments_neg_sentiment)
