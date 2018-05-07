from setuptools import setup, find_packages

with open('readme.txt') as f:
    ld = f.read()
setup(
name='runescapeapi',
version='0',
description='grandexchange, highscores, beasts, runemetrics',
long_description=ld,
author='raatty',
py_modules=["runesapeapi"],
install_requires=['wikia'],
python_requires='>=3',
license='MIT',
packages=find_packages()
)
