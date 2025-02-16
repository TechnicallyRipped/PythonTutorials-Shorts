

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

@app.errorhandler(404)
def page_not_found(e):
    print(e.code)
    print(e.description)
    return "Sorry, page not found :(",404

if __name__ == "__main__":
    app.run(debug=True)





