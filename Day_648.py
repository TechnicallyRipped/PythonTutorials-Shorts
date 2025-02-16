

from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return('Homepage')

@app.route('/profile')
def profile():
    return('This is your profile')

@app.route('/feed')
def feed():
    return redirect('home')

if __name__ == "__main__":
    app.run(debug=True)
















