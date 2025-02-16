

from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
        return('Homepage')

@app.route('/greet')
def greet():
      greeting = request.args.get('g',default='hello')
      name = request.args.get('n',default='dude')
      return f'{greeting} {name}'   

if __name__ == "__main__":
    app.run(debug=True)
















