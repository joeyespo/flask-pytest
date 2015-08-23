Flask-pytest
============

[![Current version on PyPI](http://img.shields.io/pypi/v/flask-pytest.svg)](http://pypi.python.org/pypi/flask-pytest)

Runs pytest in a background process when DEBUG is True.


Motivation
----------

Running tests shouldn't be something you have to remember to do. With this,
Flask extension, tests be automatically be run for you and re-run when
code changes.


Installation
------------

```bash
$ pip install flask-pytest
```


Usage
-----

```python
from flask import Flask
from flask.ext.pytest import FlaskPytest

app = Flask(__name__)
app = FlaskPytest(app)

app.config['DEBUG'] = True

# ...

app.run()
```

Your tests will now be run in the background whenever `DEBUG=True`. If a test
fails, you'll hear a beep and see the output. Change a file to re-run them to
see if you fixed the problem.


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository, make your changes, and add yourself to [Authors.md](AUTHORS.md)]
3. Send a pull request

If your PR has been waiting a while, feel free to [ping me on Twitter](http://twitter.com/joeyespo).
