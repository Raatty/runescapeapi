from setuptools import setup, find_packages

with open('readme.txt') as f:
    ld = f.read()
setup(
    name='runescapeapi',
    version='2',
    description='grandexchange, highscores, beasts, runemetrics',
    long_description=ld,
    long_description_content_type="text/plain",
    author='raatty',
    py_modules=["runesapeapi"],
    install_requires=['requests'],
    python_requires='>=3',
    license='MIT',
    packages=find_packages()
)
