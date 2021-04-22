all: black isort mypy flake8

run:
	pipenv shell pipenv install

exec:
	python sample.py

black:
	black ./

isort:
	isort ./

mypy:
	mypy ./

flake8:
	flake8 ./
