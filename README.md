# curs_vcgj_25_441_animale

# `tigru`
===================================

# Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Structură directoare](#structură-directoare)
3. [Rularea aplicației](#rularea-aplicației)
4. [Testare unitară](#testare-unitară)
5. [Verificare cod cu pylint](#verificare-statică-cu-pylint)
6. [Containerizare Docker](#containerizare-docker)
7. [CI/CD cu Jenkins](#cicd-cu-jenkins)
8. [Bibliografie](#bibliografie)

---

# Descriere aplicație

Această aplicație a fost realizată ca temă în cadrul cursului **Servicii Cloud și Containerizare (SCC)** – 2025.

Aplicația este scrisă în Python și oferă o interfață simplă prin Flask, unde sunt prezentate informații despre animalul ales: **Tigrul**.  
Utilizatorul poate accesa din browser descrierea, habitatul și alimentația tigrului.

Aplicația este testabilă, containerizată cu Docker și automatizată printr-un pipeline Jenkins.

---

# Structură directoare

```text
├── Dockerfile
├── Jenkinsfile
├── quickrequirements.txt
├── README.md
├── tigru.py
├── app/
│   ├── __init__.py
│   ├── lib/
│   │   ├── __init__.py
│   │   └── helper.py
│   └── tests/
│       ├── __init__.py
│       └── test_tigru.py
````

---

# Rularea aplicației

### Activare venv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r quickrequirements.txt
python3 tigru.py
```

Acces din browser la:

```
http://127.0.0.1:5000/tigru
```

---

# Testare unitară

Comandă de rulare locală:

```bash
PYTHONPATH=$PWD python3 -m unittest discover -s app/tests -p "test_*.py"
```

---

# Verificare statică cu pylint

```bash
pylint app/lib/helper.py
pylint app/tests/test_tigru.py
```

---

# Containerizare Docker

### Build:

```bash
docker build -t tigru-app .
```

### Rulare:

```bash
docker run -p 5000:5000 tigru-app
```

---

# CI/CD cu Jenkins

Pipeline-ul automat include:

* Clonare repository
* Instalare dependențe
* Rulare teste unitar
* Build imagine Docker

![jenkins](https://upload.wikimedia.org/wikipedia/commons/e/e9/Jenkins_logo.svg)

---

# Bibliografie

* Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* Dockerfile guide: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
* Jenkins Pipeline docs: [https://www.jenkins.io/doc/book/pipeline/](https://www.jenkins.io/doc/book/pipeline/)
* Python unittest: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
* Pylint: [https://pylint.pycqa.org/](https://pylint.pycqa.org/)

````

---

📌 După ce îl salvezi:

```bash
nano README.md
git add README.md
git commit -m "Adaug README.md final pentru tema Tigru"
git push
````


