# Imagine de bază
FROM python:3.9-slim

# Directorul de lucru în container
WORKDIR /app

# Copiază tot conținutul local în container
COPY . .

# Instalare Flask
RUN pip install flask

# Expune portul 9090
EXPOSE 9090

# Comanda de rulare a aplicației
CMD ["python", "animale.py"]
