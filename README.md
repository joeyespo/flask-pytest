Flask-pytest
============

[![Current version on PyPI](http://img.shields.io/pypi/v/flask-pytest.svg)](http://pypi.python.org/pypi/flask-pytest)

Runs pytest in a background process when DEBUG is True.


Motivation
----------

Running tests shouldn't be something you have to go out of your way to do. With
this Flask extension, tests will be automatically be run for you, and re-run
when code changes. It also beeps when there's an error and shows the results in
the same terminal as your Flask output.


Installation
------------

```bash
$ pip install flask-pytest
```


Usage
-----

Add `app = FlaskPytest(app)` to your project:

```python
from flask import Flask
from flask.ext.pytest import FlaskPytest

app = Flask(__name__)
app.config.from_pyfile('settings.py')

app = FlaskPytest(app)  # <-- Add this line

@app.route('/')
def hello():
    return 'Hello World!'

app.run()
```

##### settings.py

```python
DEBUG = True
```

Your tests will now be run in the background:

```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with reloader
Running tests...
...
3 passed in 1.20 seconds
```

If a test fails, you'll hear a beep and see the output. Change a source file to
reload the development server like normal, which will now re-run the tests.


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository, make your changes, and add yourself to [Authors.md](AUTHORS.md)
3. Send a pull request

If your PR has been waiting a while, feel free to [ping me on Twitter](http://twitter.com/joeyespo).
