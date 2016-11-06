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


@ask.intent("subRedditIntent")
def subRedditBrowse():
    statementText = "You have entered the Donald"
    return statement(statementText)

@ask.intent("readComments")
def readComments():
    commentText1 = "comment 1"
    commentText2 = "comment 2"
    return statement(commentText1)

@ask.session_ended
#End session.
def session_ended():
    statementText = "Goodbye, buddy"
    return statement(statementText)


if __name__ == '__main__':
    app.run(debug=True)
