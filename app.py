from flask import Flask

app = Flask(__name__)

notes = []

@app.route("/")
def hello_world():
    return "<p>Welcome to my note app!</p><a href='/new_note'>click me to add a new note</a>"