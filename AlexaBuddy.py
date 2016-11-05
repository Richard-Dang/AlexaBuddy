import praw
user_agent = "AlexaBuddy 1.0 by /u/alexabuddy"
r = praw.Reddit(user_agent=user_agent)
r.set_oauth_app_info(client_id='FP4sj6FgPVoWZA',\
                     client_secret='7j_TQb_M2tRTICl-nXvgUkTobLA',\
                     redirect_uri='http://127.0.0.1:65010/authorize_callback')
url = r.get_authorize_url('uniqueKey','identity read submit',True)
import webbrowser
webbrowser.open(url)
access_information = r.get_access_information('YLUS38aIAb1-5RKxFm8ZSes_gGk')
r.set_access_credentials(**access_information)
authenticated_user = r.get_me()
print authenticated_user.name, authenticated_user.link_karma
r.refresh_access_information(access_information['refresh_token'])
submissions = r.get_subreddit('news').get_top(limit=10)
for x in submissions:
    print x