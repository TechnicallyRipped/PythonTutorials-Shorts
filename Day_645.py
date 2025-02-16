
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    css_ = url_for('static',filename='styles.css')
    return render_template('wCSS.html',
                           css_path=css_)

if __name__ == "__main__":
    app.run(debug=True)