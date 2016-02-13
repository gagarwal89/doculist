import os
from flask import (
    Flask,
    render_template,
    request,
    redirect
)

app = Flask(__name__, template_folder='static', static_folder='static')


@app.route("/")
def serve_main_page():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    form = request.form
    name = form['name']
    email = form['email']
    password = form['password']

    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
