from python:3.10-alpine

run adduser -D lemur
workdir /home/lemur/app

copy lemur.py .
copy requirements.txt requirements.txt

run python3 -m venv .venv && \
	.venv/bin/pip install --upgrade pip && \
	.venv/bin/pip install -r requirements.txt

cmd [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "lemur:app"]
 
