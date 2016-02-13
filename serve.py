import os
from flask import (
    Flask,
    render_template,
    request,
    redirect
)

from models import NewUser
from database import create_user

app = Flask(__name__, template_folder='static', static_folder='static')


@app.route("/")
def serve_main_page():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    form = request.form
    new_user = NewUser(form)
    create_user(new_user)
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    email = form['email']
    password = form['password']

    return redirect('/p')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
