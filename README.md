# curs_vcgj_25_441_animale
# Vidra
============================

## Cuprins
1. [Descriere aplicație](#descriere-aplicație)
2. [Versiune și status](#versiune-și-status)
   1. [Probleme cunoscute](#probleme-cunoscute)
3. [Configurare și rulare](#configurare-și-rulare)
4. [Testare](#testare)
5. [Verificare calitate cod cu pylint](#verificare-calitate-cod-cu-pylint)
6. [DevOps – CI/CD](#devops---ci/cd)
   1. [Pipeline Jenkins](#pipeline-jenkins)
7. [Containerizare](#containerizare)
8. [Stadiu dezvoltare branch](#stadiu-dezvoltare-branch)
9. [Bibliografie](#bibliografie)

---

## Descriere aplicație

**Vidra** este o aplicație web scrisă în Python, care utilizează framework-ul Flask. Scopul aplicației este de a demonstra integrarea între cod Python, testare automată, analiză statică și livrare automată folosind Jenkins și Docker.

Aplicația are un fișier principal `vidra.py` și o structură simplă pentru testare și analiză statică. Este potrivită pentru demonstrarea unui pipeline DevOps complet.

---

## Versiune și status
**v1.0 – funcționalitate minimă completă**
- Inițializare proiect
- Flask server de bază funcțional
- Integrare Jenkins și Docker

### Probleme cunoscute
- Lipsă acoperire completă prin teste unitare
- Lipsă interfață grafică HTML (doar cod backend de bază)

---

## Configurare și rulare

### 1. Activare mediu virtual și instalare dependințe

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Rulare aplicație local (pentru dezvoltare)

```bash
python3 vidra.py
```

Aplicația va fi disponibilă la:  
📍 `http://127.0.0.1:5000/`

---

## Testare

### 1. Testare automată

```bash
python3 -m unittest app.test.testare
```

Testele verifică funcționalitatea aplicației și sunt integrate și în pipeline-ul Jenkins.

---

## Verificare calitate cod cu pylint

```bash
pylint vidra.py || true
```

Se verifică stilul codului, denumirea variabilelor și alte reguli PEP8.

---

## DevOps – CI/CD

### Pipeline Jenkins

Fișierul `Jenkinsfile` definește următorii pași:
- Build & Setup venv
- Pylint - Calitate cod
- Unit Testing
- Docker Build & Deploy

Configurarea este complet funcțională și automatizată la fiecare push în GitHub.

---

## Containerizare

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "vidra.py"]
```

### Comenzi:

```bash
docker build -t vidra:v1 .
docker run -d -p 8020:5000 vidra:v1
```

---

## Stadiu dezvoltare branch

### Funcționalitatea adăugată:
- Server Flask în `vidra.py`
- Suport complet pentru testare, analiză și containerizare

### Stadiul implementării:
Cod, testare și livrare complet funcționale

### Testele efectuate:
- `unittest` local și în Jenkins
- `pylint` rulare statică
- Container Docker testat

### Integrare:
- PR deschis pentru integrarea în `main`

### Pull Request-uri:
- `PR#17` – Integrare Vidra
- Review efectuat și aprobat

---

## Bibliografie

- https://flask.palletsprojects.com/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/get-started/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://docs.github.com/en/actions
