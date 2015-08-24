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

__version__ = '0.0.2'


BEEP_CHARACTER = '\a'


def bool_config(app, setting, default=None):
    value = app.config.get(setting)
    return (default
            if value is None else
            str(app.config.get(setting)).lower() == 'true')


def call_then_log(beep=True, exitfirst=True, quiet=True, extra_args=None):
    argv = []
    if exitfirst:
        argv += ['--exitfirst']
    if quiet:
        argv += ['--quiet']
    argv += extra_args or []

    exit_code = pytest.main(argv)
    if exit_code != 0 and beep:
        print(BEEP_CHARACTER, end='')


def start_tests(beep=True, exitfirst=True, quiet=True, extra_args=None):
    # TODO: Use multiprocessing
    print('Running tests...')
    thread = Thread(target=call_then_log, name='background-pytest', args=(
        beep, exitfirst, quiet, extra_args))
    thread.daemon = True
    thread.start()


def FlaskPytest(app, extra_args=None):
    inner_run = app.run

    def run_app(*args, **kwargs):
        if (app.debug and os.environ.get('WERKZEUG_RUN_MAIN') and
                bool_config(app, 'FLASK_PYTEST_ENABLED', True)):
            start_tests(
                beep=bool_config(app, 'FLASK_PYTEST_BEEP', True),
                exitfirst=bool_config(app, 'FLASK_PYTEST_EXITFIRST', True),
                quiet=bool_config(app, 'FLASK_PYTEST_QUIET', True))
        return inner_run(*args, **kwargs)

    # Override the built-in run method and return the app
    app.run = run_app
    return app
