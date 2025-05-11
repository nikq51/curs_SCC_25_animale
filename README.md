
# curs_SCC_25_441_animale

# `cal`

---

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Structură directoare](#structură-directoare)
3. [Rularea aplicației](#rularea-aplicației)
4. [Testare unitară](#testare-unitară)
5. [Containerizare Docker](#containerizare-docker)
6. [CI/CD cu Jenkins](#cicd-cu-jenkins)
7. [Bibliografie](#bibliografie)

---

## Descriere aplicație

Această aplicație a fost realizată ca temă în cadrul cursului **Servicii Cloud și Containerizare (SCC)** – 2025.

Aplicația este scrisă în Python și oferă o interfață simplă prin Flask, unde sunt prezentate informații despre animalul ales: **Calul**.  
Utilizatorul poate accesa din browser descrierea, culoarea și alte informații despre cal.

Aplicația este testabilă, containerizată cu Docker și automatizată printr-un pipeline Jenkins.

---

## Structură directoare

```text
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
├── app/
│   ├── 441D_animale.py              # Scriptul principal Flask
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_animale.py    # Funcții specifice pentru Cal
│   └── tests/
│       ├── __init__.py
│       └── test_cal.py              # Teste unitar pentru Flask API


##Rularea aplicatiei

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app/441D_animale.py

## Acces din browser
http://localhost:5000/cal
http://localhost:5000/cal/culoare
http://localhost:5000/cal/descriere

##Testare unitara

PYTHONPATH=$PWD python3 -m unittest discover -s app/tests -p "test_*.py"

## Containerizare Docker

docker build -t flask_app_cal .

docker run -d --name flask_app_cal_container -p 5000:5000 flask_app_cal

##CI/CD cu Jenkins

Pipeline-ul automat include următorii pași:

    Clonare repository - GitHub → Jenkins

    Build imagine Docker - Se creează imaginea Docker pentru aplicație

    Rulare teste unitar - Se verifică funcționarea endpoint-urilor

    Pornire container Docker - Se rulează containerul pe portul 5000

    Testare endpoint-uri - Testare finală cu curl pentru validare

##Bibliografie

Flask documentation: https://flask.palletsprojects.com/

Dockerfile guide: https://docs.docker.com/engine/reference/builder/

Jenkins Pipeline docs: https://www.jenkins.io/doc/book/pipeline/

Python unittest: https://docs.python.org/3/library/unittest.html

Pylint: https://pylint.pycqa.org/
