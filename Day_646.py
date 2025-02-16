

from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    image = url_for('static',filename='red.png')
    return render_template('pic.html',
                           pic=image)

if __name__ == "__main__":
    app.run(debug=True)