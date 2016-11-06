import praw
import webbrowser
import re
import MessageGrader

user_agent = "AlexaBuddy 1.0 by /u/alexabuddy"
r = praw.Reddit(user_agent=user_agent)

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

def get_top_posts(subreddit, num_posts):
    posts = []
    submissions = r.get_subreddit(subreddit).get_top(limit=num_posts)
    for x in submissions:
        title = re.search('(?<=::).*',str(x))
        posts.append(title.group(0))

    return posts



top_news_posts = get_top_posts('news',10)
print MessageGrader.gradeMultiple(top_news_posts)