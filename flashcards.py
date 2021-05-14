from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())


# Add a page that shows how many times it has been viewed
counter = 0

@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "This page was served " +str(counter) + " times"
