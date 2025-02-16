

from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
        return('Homepage')

@app.route('/hello')
def hello_():
      name = request.args.get('name',default='Joe')
      return f'Hello {name}'   

if __name__ == "__main__":
    app.run(debug=True)
















