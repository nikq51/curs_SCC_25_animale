FROM python:3.10-alpine

# Creează un utilizator non-root numit caine
RUN adduser -D caine

# Setează directorul de lucru
WORKDIR /home/caine/app

# Copiază fișierele aplicației
COPY caine.py .
COPY requirements.txt requirements.txt

# Creează un mediu virtual și instalează dependențele
RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

# Setează utilizatorul non-root pentru execuție
USER caine

# Expune portul 5050 (Flask)
EXPOSE 5050

# Rulează aplicația cu gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5050", "caine:app"]
