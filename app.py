from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<p>Jello World</p>"
