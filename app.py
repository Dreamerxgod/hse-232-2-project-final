from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        message = request.form['message']
        return 'Thank you for your feedback!'
    return render_template('feedback.html')




@app.route('/analytics')
def analytics():
    return render_template("fifastatsss.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()