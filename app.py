from flask import Flask, request, render_template, url_for
from jinja2 import Environment

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')
def submit():
    username = request.values.get('usernameText')
    password = request.values.get('passwordText')

    if password == 'sliit123':
        return render_template('home.html', greeting=" Welcome %s"%(username))
    else: 
        return render_template('index.html', message="Invalid credentials!")


if __name__ == "__main__":
    app.run(debug=True)