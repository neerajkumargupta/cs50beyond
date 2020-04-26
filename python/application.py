from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"


@app.route("/<string:name>")
def index1(name):
    now = datetime.datetime.now()
    is_newYears = now.month == 1 and now.day == 1
    return render_template("index.html",is_newYears=is_newYears)

if __name__ == "__main__":
    app.run(debug=True)