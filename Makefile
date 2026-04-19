install:
	python -m venv venv
	./venv/Scripts/pip install -r requirements.lock.txt

run:
	./venv/Scripts/python app.py

test:
	./venv/Scripts/python -m pytest test_app.py

lint:
	./venv/Scripts/python -m flake8 app.py