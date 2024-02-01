from flask import Flask
import os

app = Flask(__name__)

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

# TODO: remove debug flag and change host
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
