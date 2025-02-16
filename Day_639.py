

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the homepage"

@app.route("/tech")
def tech():
    return "TechnicallyRipped!"

if __name__ == "__main__":
    app.run(debug=True)







