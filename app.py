from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Python Advanced after update in March 2022! - Gewoon om het af te leren -v2'


if __name__ == '__main__':
    app.run()
