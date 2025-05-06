# Use a lightweight Python image
FROM python:3.8-alpine

# Creează un utilizator non-root numit "student"
RUN adduser -D student

# Rulează comenzile ca utilizatorul "student"
USER student

# Setează directorul de lucru în container
WORKDIR /home/student/

# Copiază fișierele din contextul local în container
COPY app app
COPY animale.py animale.py

# Creează un mediu virtual și instalează Flask direct
RUN python3 -m venv .venv
RUN .venv/bin/pip install Flask

# Expune portul pe care aplicația Flask îl va folosi
EXPOSE 5000

# Comanda care pornește aplicația
CMD [".venv/bin/python", "animale.py"]
