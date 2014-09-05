from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def map():
    return render_template("map.html")

@app.route("/hello")
def hello():
    return "Hello Moto!"

if __name__ == "__main__":
    app.run(debug=True) # enable auto-refresh and a bunch of other cool stuff

