all: black isort mypy flake8

run:
	pipenv shell pipenv install

exec:
	python main.py

black:
	black ./

isort:
	isort ./

mypy:
	mypy ./

flake8:
	flake8 ./
