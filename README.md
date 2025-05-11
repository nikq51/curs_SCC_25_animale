# Proiect: Vultur

## Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
2. [Versiune si status](#versiune-si-status)
    - [Probleme cunoscute](#probleme-cunoscute)
3. [Configurare si rulare](#configurare-si-rulare)
4. [Testare](#testare)
5. [Analiza statica cu pylint](#analiza-statica-cu-pylint)
6. [DevOps - CI/CD](#devops---cicd)
    - [Pipeline Jenkins](#pipeline-jenkins)
7. [Containerizare cu Docker](#containerizare-cu-docker)
8. [Stadiu dezvoltare](#stadiu-dezvoltare)
9. [Bibliografie](#bibliografie)

---

## Descriere aplicatie

**Vultur** este o aplicatie de tip microserviciu scrisa in Python, care utilizeaza framework-ul Flask. Aplicatia este dezvoltata pentru a demonstra o arhitectura simplificata de tip DevOps, cu accent pe:
- testare unitară
- analiza statica a codului
- integrare si livrare continua (CI/CD)
- containerizare cu Docker

Fisierul principal este `vultur.py`, iar codul este organizat modular pentru a permite extinderea si colaborarea in echipa.

---

## Versiune si status

**v1.0 - versiune functionala stabila**
- Aplicatie complet functionala si rulabila
- Testata local si automat in Jenkins
- Pipeline CI/CD si containerizare functionala

### Probleme cunoscute
- Structura modulara simpla (fara blueprint-uri Flask)
- Lipsa functionalitatilor avansate (autentificare, sesiuni etc.)

---

## Configurare si rulare

### 1. Setup mediu virtual si instalare dependinte
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
Acces aplicatie: `http://127.0.0.1:5000/`

---

## Testare

Aplicatia contine teste unitare care acopera rutele Flask.

### Rulare teste:
```bash
python3 -m unittest discover -s app/test -p "testare.py"
```

---

## Analiza statica cu pylint

Poti rula pylint pentru a analiza codul Python:
```bash
pylint Vultur.py app/lib/*.py app/test/*.py || true
```

Aceasta comanda verifica:
- stilul codului
- respectarea conventiilor PEP8
- utilizarea corecta a variabilelor si importurilor

---

## DevOps - CI/CD

### Pipeline Jenkins

Configuratia pipeline-ului se afla in fisierul `Jenkinsfile` si include:
- configurare mediu virtual
- analiza statica cu pylint
- rulare teste unitare cu unittest
- build si rulare container Docker

Pipeline-ul poate fi rulat manual din Jenkins sau automat prin webhook GitHub.

---

## Containerizare cu Docker

### Dockerfile utilizat
```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "vultur.py"]
```

### Comenzi uzuale
```bash
VERSION=1.0.0  # sau orice versiune dinamica

docker build -t vultur:v$VERSION .
docker run -d -p 8020:5000 vultur:v$VERSION
```

Aplicatia va fi disponibila la `http://localhost:8020`

---

## Stadiu dezvoltare

### Functionalitati implementate:
- Aplicatie Flask complet functionala
- Teste unitare cu unittest
- Linting cu pylint
- Pipeline CI/CD in Jenkins
- Docker pentru build si deploy

### Teste efectuate:
- unittest complet (testare rute)
- pylint (analiza statica)
- build + rulare automata in Jenkins

### Integrare Git:
- Branch: `devel_vultur_nume`
- Pull request creat catre `main`

---

## Bibliografie
- https://flask.palletsprojects.com/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/
- https://chat.openai.com/ (ChatGPT)

