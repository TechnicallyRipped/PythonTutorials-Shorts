
from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    move_to = url_for('go_to_page2')
    return render_template('home_button.html',
                           click=move_to)

@app.route('/page2')
def go_to_page2():
    move_to = url_for('home')
    return render_template('page2.html',
                           click=move_to)

if __name__ == "__main__":
    app.run(debug=True)