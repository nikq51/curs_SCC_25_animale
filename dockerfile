# Imagine de bază Python minimală
FROM python:3.10-alpine

# Creare utilizator non-root pentru rulare sigură
RUN adduser -D puma

# Setare director de lucru
WORKDIR /home/puma/app

# Copiere fișiere esențiale în imagine
COPY puma.py .
COPY quickrequirements.txt .

# Instalare dependențe în mediu virtual
RUN python3 -m venv .venv && \
    .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r quickrequirements.txt

# Comutare utilizator
USER puma

# Port expus de aplicație Flask
EXPOSE 5001

# Pornire aplicație cu Gunicorn (mod producție)
CMD [".venv/bin/gunicorn", "-b", "0.0.0.0:5001", "puma:app"]
