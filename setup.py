from setuptools import setup, find_packages

with open('readme.txt') as f:
    ld = f.read()
setup(
name='runescapeapi',
version='0',
description='grandexchange, highscores, beasts, runemetrics',
long_description=ld,
long_description_content_type='text/plain',
author='raatty',
author_email='me@raatty.club',
py_modules=["runesapeapi"],
install_requires=['wikia'],
)