#!/usr/bin/env python

import logging
import reddit_analysis

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

# TODO:
# - Fix unicode
# - Add pause after post number

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

subreddit_arg = ""
num_of_posts_arg = 0
neg_sentiment_arg = []
choice_arg = ""


@ask.launch

def welcome():

    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("SubRedditIntent", convert={'subreddit': str})

def ask_num_posts(subreddit):
    global subreddit_arg
    subreddit_arg = subreddit
    num_posts = render_template('ask_posts')

    return question(num_posts)

@ask.intent("NumOfPostsIntent", convert={'num_of_posts': int})

def read_post_titles(num_of_posts):
    global num_of_posts_arg
    global pos_sentiment_arg
    global neg_sentiment_arg

    num_of_posts_arg = num_of_posts

    top_news_posts = reddit_analysis.get_top_posts(subreddit_arg, num_of_posts_arg)
    sentiment_dict = reddit_analysis.gradeMultiple(top_news_posts)

    pos_sentiment = sentiment_dict[0]
    neg_sentiment_arg = sentiment_dict[1]

    read_posts = render_template('read_pos_posts', posts=pos_sentiment)

    return question(read_posts)


@ask.intent("ContinueIntent")

def read_decision():

    if len(neg_sentiment_arg) > 0:
        # @ask.intent("ChoiceIntent", convert={'choice': str})
        # def read_choice_question(choice):
        #     global choice_arg
        #     choice_arg = choice
        #     choice_msg = render_template('negative')
        #     return
        return_result_msg = render_template('negative')
        return question(return_result_msg)
        # if choice_arg == "yes":
        #     read_posts = render_template('read_posts', posts=neg_sentiment_arg)
        #     return statement(read_posts)
        # else:
        #     goodbye_msg = render_template('goodbye')
        #     return statement(goodbye_msg)
    else:
        return_result_msg = render_template('goodbye')
        return statement(return_result_msg)

@ask.intent("NegativeIntent")

def say_neg_messages():
    read_posts = render_template('read_neg_posts', posts=neg_sentiment_arg)
    return statement(read_posts)



if __name__ == '__main__':

    app.run(debug=True)