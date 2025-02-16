

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

@app.route('/api')
def api_response():
    data = {'Text':'Hello World',
            'Channel':'TechnicallyRipped'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
















