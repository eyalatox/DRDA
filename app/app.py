from flask import Flask

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

# TODO: remove debug flag and change host
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
