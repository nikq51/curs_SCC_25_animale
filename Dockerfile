# Imagine de bază
FROM python:3.9-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază tot proiectul în container
COPY . .

# Instalează Flask
RUN pip install flask

# Expune portul folosit în aplicație
EXPOSE 7070

# Comanda care pornește aplicația Flask
CMD ["python", "animale.py"]
