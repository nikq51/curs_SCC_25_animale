FROM python:3.10-alpine

# Creează un user non-root
RUN adduser -D tigru

# Directorul aplicației
WORKDIR /home/tigru/app

# Copiază fișierele aplicației
COPY tigru.py .
COPY quickrequirements.txt .

# Instalează dependențele în mediu virtual
RUN python3 -m venv .venv
RUN .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r quickrequirements.txt

# Rulează aplicația ca user non-root
USER tigru

# Expune portul Flask
EXPOSE 5050

# Rulează cu Gunicorn
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5000", "tigru:app"]
