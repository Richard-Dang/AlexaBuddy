import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch()
def launch():
    questionText = "What subreddit would you like to browse?"
    return question(questionText)

<<<<<<< HEAD
@ask.intent("subRedditIntent")
def subRedditBrowse(subreddit):
    statementText = "You have entered {}".format(subreddit)
    return statement(statementText)

@ask.intent("readContentIntent")
def readContent():
    content1 = "comment 1"
    content2 = "comment 2"
=======

@ask.intent("subRedditIntent")
def subRedditBrowse():
    statementText = "You have entered the Donald"
    return statement(statementText)

@ask.intent("readComments")
def readComments():
    commentText1 = "comment 1"
    commentText2 = "comment 2"
>>>>>>> 9698d5f8b6a66431e9501dcb64692879537a9c04
    return statement(commentText1)

@ask.session_ended
#End session.
def session_ended():
    statementText = "Goodbye, buddy"
    return statement(statementText)

<<<<<<< HEAD
=======

>>>>>>> 9698d5f8b6a66431e9501dcb64692879537a9c04
if __name__ == '__main__':
    app.run(debug=True)
