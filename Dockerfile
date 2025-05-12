FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app

RUN apt-get update && apt-get install -y curl

EXPOSE 5000

CMD ["python3", "/app/cal.py"]

