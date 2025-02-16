

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
        num = 2
        return(render_template("home2.html", x=num))

if __name__ == "__main__":
    app.run(debug=True)

