SHELL = bash

install: venv
	source venv/bin/activate; \
	python3 setup.py install; \

clean:
	rm -rf venv build dist runescapeapi.egg-info

venv:
	python3 -m venv venv
