#!/usr/bin/env python

import logging
import reddit_analysis

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

subreddit_arg = ""
num_of_posts_arg = 0


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
    num_of_posts_arg = num_of_posts

    top_news_posts = reddit_analysis.get_top_posts(subreddit_arg, num_of_posts_arg)
    sentiment_dict = reddit_analysis.gradeMultiple(top_news_posts)
    pos_sentiment = sentiment_dict[0]
    neg_sentiment = sentiment_dict[1]

    read_posts = render_template('read_posts', posts=neg_sentiment)

    return statement(read_posts)


    # winning_numbers = session.attributes['numbers']
    #
    # if [first, second, third] == winning_numbers:
    #
    #     msg = render_template('win')
    #
    # else:
    #
    #     msg = render_template('lose')

    #return statement(msg)



#@ask.intent("NumPostsIntent", convert={'first': int, 'second': int, 'third': int})

#
# @ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
#
# def answer(first, second, third):
#
#     winning_numbers = session.attributes['numbers']
#
#     if [first, second, third] == winning_numbers:
#
#         msg = render_template('win')
#
#     else:
#
#         msg = render_template('lose')
#
#     return statement(msg)


if __name__ == '__main__':

    app.run(debug=True)