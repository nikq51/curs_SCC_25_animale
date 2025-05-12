FROM python:3.10-alpine

ENV FLASK_APP Nicolae_441D_Animale

RUN adduser -D animale_user

USER animale_user

WORKDIR /home/animale_user/

COPY app ./app/
COPY requirements.txt .
COPY app/Nicolae_441D_Animale.py .

RUN python3 -m venv .venv 
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD [".venv/bin/python", "app/Nicolae_441D_Animale.py"]
