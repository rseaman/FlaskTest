from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cookietest/')
def cookie():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username','Riley')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
