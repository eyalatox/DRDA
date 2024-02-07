from flask import Flask
import werkzeug.security
from flask import render_template, request, url_for, redirect, flash
import os

app = Flask("DRDA-APP")

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    return 'OK'

@app.route('/version')
def version():
    return '1.0.0'

# add a route which get a commend and run is with os.system
# the route should return the output of the command
# for example:
# GET /run?cmd=ls
# should return the exit code of ls
@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    exit_code = os.system(cmd)
    if exit_code != 0:
        print(f'error running cmd {cmd} exit_code: {exit_code}')
    return exit_code

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or not werkzeug.security.check_password_hash(users[username], password):
            error = 'Invalid username or password.'
        else:
            # Log the user in (replace with your session management or authentication system)
            flash('You were logged in successfully.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

# TODO: remove debug flag and change host
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
