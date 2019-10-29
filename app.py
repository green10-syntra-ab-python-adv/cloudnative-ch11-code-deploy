from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Python Advanced after update!'


if __name__ == '__main__':
    app.run()
