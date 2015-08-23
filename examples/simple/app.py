from flask import Flask
from flask.ext.pytest import FlaskPytest


app = Flask(__name__)
app.config.from_pyfile('settings.py')
# Extensions
app = FlaskPytest(app)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
