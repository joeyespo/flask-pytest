"""\
flask-pytest
------------

Runs pytest in a background process when DEBUG is True.
"""

from __future__ import print_function

import os
from multiprocessing import Process

import pytest

__version__ = '0.0.5'


BEEP_CHARACTER = '\a'


def bool_config(app, setting, default=None):
    value = app.config.get(setting)
    return (default
            if value is None else
            str(app.config.get(setting)).lower() == 'true')


def run_tests_sync(beep=True, exitfirst=True, quiet=True, *extra_args):
    argv = []
    if exitfirst:
        argv += ['--exitfirst']
    if quiet:
        argv += ['--quiet']
    if extra_args:
        argv += extra_args

    exit_code = pytest.main(argv)
    if exit_code != 0 and beep:
        print(BEEP_CHARACTER, end='')


def start_tests(beep=True, exitfirst=True, quiet=True, *extra_args):
    print('Running tests...')
    p = Process(target=run_tests_sync, name='background-pytest',
                args=(beep, exitfirst, quiet) + extra_args)
    p.daemon = True
    p.start()


def FlaskPytest(app, *extra_args):
    inner_run = app.run

    def run_app(*args, **kwargs):
        if (app.debug and os.environ.get('WERKZEUG_RUN_MAIN') and
                bool_config(app, 'FLASK_PYTEST_ENABLED', True)):
            start_tests(
                bool_config(app, 'FLASK_PYTEST_BEEP', True),
                bool_config(app, 'FLASK_PYTEST_EXITFIRST', True),
                bool_config(app, 'FLASK_PYTEST_QUIET', True),
                *extra_args)
        return inner_run(*args, **kwargs)

    # Override the built-in run method and return the app
    app.run = run_app
    return app
