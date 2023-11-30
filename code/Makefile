VENV = venv
PYTHON = backend/$(VENV)/bin/python3
PIP = backend/$(VENV)/bin/pip
FLASK = backend/$(VENV)/bin/flask


.PHONY: clean backend testteams 

clean: 
	rm -rf backend/venv
	rm -rf backend/__pycache__

backend: backend/venv/bin/activate
	$(FLASK) --app backend/app run

backend/venv/bin/activate: backend/requirements.txt
	python3 -m venv backend/$(VENV);
	export PYTHONPATH=.
	$(PIP) install -r backend/requirements.txt

testteams: backend/venv/bin/activate
	$(PYTHON) backend/helper.py