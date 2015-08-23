"""\
flask-pytest
------------

Runs pytest in a background process when DEBUG is True.
"""

from __future__ import print_function

import os
from threading import Thread

import pytest
from termcolor import colored

__version__ = '0.0.1'


BEEP_CHARACTER = '\a'


def call_then_log(full_run=False, verbose=False, extra_args=None):
    argv = []
    if not full_run:
        argv += ['--exitfirst']
    if not verbose:
        argv += ['--quiet']
    argv += extra_args or []

    exit_code = pytest.main(argv)
    if exit_code != 0:
        print(BEEP_CHARACTER, end='')


def run_background_tests():
    print('Running tests...')
    thread = Thread(target=call_then_log, name='background-pytest')
    thread.daemon = True
    thread.start()


def FlaskPytest(app, extra_args=None):
    inner_run = app.run

    def run_app(*args, **kwargs):
        run = str(app.config.get('FLASK_RUN_TESTS', True)).lower() == 'true'
        if (app.debug and run and os.environ.get('WERKZEUG_RUN_MAIN')):
            run_background_tests()

        result = inner_run(*args, **kwargs)
        return result

    # Override the built-in run method and return the app
    app.run = run_app
    return app
