

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

@app.route("/<name>")
def home_cust(name):
    return f"Welcome {name}!"


if __name__ == "__main__":
    app.run(debug=True)
















