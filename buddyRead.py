import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def launch():
    statementText = "Hello, I am AlexaBuddy."
    questionText = "What subreddit would you like to browse?"
    return statement.(statementText).question.(questionText)



@ask.session_ended
# End session.
def session_ended():
    return
