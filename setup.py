"""\
flask-pytest
------------

Runs pytest in a background process when DEBUG is True.


Links
`````

* `Website <http://github.com/joeyespo/flask-pytest>`_

"""

import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='flask-pytest',
    version='0.0.2',
    description='Runs pytest in a background process when DEBUG is True.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/flask-pytest',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=read('requirements.txt'),
)
