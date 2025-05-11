# Vultur
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

**Vultur** este o aplicație de tip microserviciu scrisă în Python, care utilizează framework-ul Flask. Aplicația este dezvoltată pentru a demonstra o arhitectură simplificată de tip DevOps, cu accent pe testare, analiză statică a codului și automatizare prin Jenkins și Docker.

Fișierul principal este `vultur.py`, iar codul este organizat clar pentru extindere viitoare și colaborare în echipă.

---

## Versiune și status
**v1.0 – versiune funcțională stabilă**
- Implementare corectă și rulabilă
- Testată în medii locale și în Jenkins
- Pipeline și containerizare complet configurate

### Probleme cunoscute
- Structura modulară minimă (momentan fără blueprint-uri Flask)
- Nu include funcții avansate (ex: autentificare, sesiuni)

---

## Configurare și rulare

### 1. Setup mediu virtual și instalare dependințe

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Lansare server local

```bash
python3 vultur.py
```

Aplicația este accesibilă la:  
📍 `http://127.0.0.1:5000/`

---

## Testare

### 1. Rulare teste

Aplicația include un fișier de testare cu `unittest`, rulabil cu:

```bash
python3 -m unittest app.test.testare
```

Testele acoperă comportamentul rutelor definite în aplicație.

---

## Verificare calitate cod cu pylint

```bash
pylint vultur.py || true
```

Se verifică stilul, utilizarea variabilelor, organizarea funcțiilor și respectarea regulilor Python.

---

## DevOps – CI/CD

### Pipeline Jenkins

Pipeline-ul este configurat în `Jenkinsfile` și include:

- Configurare mediu de lucru
- Analiză statică
- Testare automată
- Build și deploy Docker

Acesta rulează automat la push în GitHub și oferă feedback imediat.

---

## Containerizare

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "vultur.py"]
```

### Comenzi uzuale:

```bash
docker build -t vultur:v1 .
docker run -d -p 8023:5000 vultur:v1
```

Aplicația va putea fi accesată la `http://localhost:8023`.

---

## Stadiu dezvoltare branch

### Funcționalități finalizate:
- Server Flask + endpoint principal
- Teste unitare de bază
- Analiză cod + Docker integrate în CI

### Teste efectuate:
- Verificare `unittest`
- Verificare `pylint`
- Rulare completă în Jenkins + Docker

### Integrare:
- Branch `devel_vultur_nume`
- Pull request creat pentru integrarea în `main`

---

## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/
