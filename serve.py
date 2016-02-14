import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session
)

from models import NewUser, LoginUser
from database import create_user, get_user

app = Flask(__name__, template_folder='static', static_folder='static')


@app.route("/")
def serve_main_page():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    form = request.form
    new_user = NewUser(form)
    uuid = create_user(new_user)

    if uuid is None:
        return redirect('/')

    session['uuid'] = uuid
    return redirect('/home')


@app.route('/login', methods=['POST'])
def login():
    form = request.form

    user = LoginUser(form)
    uuids = get_user(user)

    if uuids is None or len(uuids) != 1:
        return redirect('/')

    session['uuid'] = uuids[0]
    return redirect('/home')


@app.route('/home')
def home():
    uuid = session['uuid']
    print uuid
    return render_template('profile.html')

if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SECRET_KEY'] = 'super secret key'
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
