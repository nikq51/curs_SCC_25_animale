FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app

EXPOSE 5000

CMD ["python3", "/app/441D_animale.py"]

