#takes flask c;ass from flask Module

from flask import Flask

#Create a Flask web application and store it in variable "app"

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This is my simple web app."

@app.route("/about")
def about():
    return "This app is deployed using CI/CD."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)