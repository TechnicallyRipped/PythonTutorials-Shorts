

from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
        return('Homepage')

@app.route('/search')
def search_():
      word = request.args.get('word')
      if word:
            return(f'You searched for {word}!')
      else:
            return('Search for something!')      

if __name__ == "__main__":
    app.run(debug=True)



