FROM python:3.10-alpine

RUN adduser -D koala
WORKDIR /home/koala/app

COPY koala.py .
COPY requirements.txt requirements.txt

RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "koala:app"]
