from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def referrals():
    return render_template("referrals.html", title="Hello")

@app.route("/start")
def hello_world():
    return render_template("index.html", title="Hello")

if __name__ == "__main__":
    app.run(debug=True, host='::', port=5000)  # Listen on all available interfaces
