# Aplicația Animale - Manul
===================================

## Cuprins
1. [Descriere aplicație](#descriere-aplicație)
2. [Versiune și status](#versiune-și-status)
    1. [Probleme cunoscute](#probleme-cunoscute)
3. [Configurare și rulare](#configurare-și-rulare)
4. [Testare](#testare)
5. [Verificare calitate cod cu Pylint](#verificare-calitate-cod-cu-pylint)
6. [DevOps – CI/CD](#devops---cicd)
   1. [Pipeline Jenkins](#pipeline-jenkins)
7. [Containerizare](#containerizare)
8. [Stadiu dezvoltare branch (Contribuția Mea)](#stadiu-dezvoltare-branch-contribuția-mea)
9. [Bibliografie (Opțional)](#bibliografie-opțional)

---

## Descriere aplicație

**Aplicația Animale - Manul** este o componentă a unui proiect mai larg dezvoltat în Python, utilizând framework-ul Flask. Scopul este de a demonstra un flux de lucru DevOps complet, incluzând dezvoltare, testare automată, analiză a calității codului, integrare continuă cu Jenkins și containerizare cu Docker.

Această componentă specifică se concentrează pe prezentarea de informații despre animalul Manul. Fișierul principal al aplicației este `app/Nicolae_441D_Animale.py`, iar funcționalitățile specifice Manulului sunt definite în `app/lib/biblioteca_Animale.py`.

---

## Versiune și status
**v1.0 – Funcționalitate de bază pentru Manul**
- Componentele esențiale pentru afișarea informațiilor despre Manul sunt funcționale.
- Codul este testat (funcționalități de bază) și analizat cu Pylint.
- Integrarea în pipeline-ul Jenkins și containerizarea sunt funcționale.

### Probleme cunoscute
- Interfața web este minimă, generată direct ca HTML în Python.

---

## Configurare și rulare

### 1. Creare mediu virtual și instalare pachete
Asigurați-vă că sunteți în directorul rădăcină al proiectului.
```bash
# Folosind scriptul customizat din proiect
source ./activeaza_venv 
```

### 2. Lansare aplicație

```bash
./ruleaza_aplicatia
```

Aplicația pornește pe adresa:
📍 `http://127.0.0.1:5001/`

---

## Testare

### 1. Executare teste

Testele sunt definite în directorul tests/ . Pentru a le rula (cu mediul virtual activat):

```bash
pytest
```

Testele validează funcțiile din app/lib/biblioteca_Animale.py.

---

## Verificare calitate cod cu pylint

```bash
pylint app/lib/biblioteca_Animale.py || true
pylint app/Nicolae_441D_Animale.py || true
pylint tests/test_app.py || true
```

Analiza codului este parte din pipeline-ul Jenkins.

---

## DevOps – CI/CD

### Pipeline Jenkins

`Jenkinsfile` definește etapele de build, testare și livrare:

- Setup mediu virtual și instalare dependențe (Build & Setup venv)
- Analiză statică a codului cu Pylint (Pylint - Calitate cod)
- Rularea testelor unitare cu Pytest (Unit Testing cu pytest)
- Construirea imaginii Docker (Docker Build & Deploy - include build, curățare container vechi, rulare container nou)

Acest pipeline rulează automat la fiecare modificare în branch.

---

## Containerizare

```dockerfile
FROM python:3.10-alpine
ENV FLASK_APP Nicolae_441D_Animale
RUN adduser -D animale_user
USER animale_user
WORKDIR /home/animale_user/
COPY app ./app/
COPY requirements.txt .
COPY app/Nicolae_441D_Animale.py .
RUN python3 -m venv .venv 
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD [".venv/bin/python", "Nicolae_441D_Animale.py"]
```

### Comenzi utile:

```bash
docker build -t animale-app:v1.0 .
docker run -d -p 5001:5001 --name animale-container animale-app:v1.0
```

Acces aplicație: `http://localhost:5001`

---

## Stadiu dezvoltare branch

### Implementare:
- Dezvoltarea funcționalităților pentru animalul Manul (Pisica Pallas)
- CI/CD și containerizare validate

### Testare efectuată:
- Teste unitare pentru funcțiile Manul (cu pytest). Analiză statică a codului (cu Pylint)
- Build Docker testat în Jenkins

### Integrare:
- Branch activ: `devel_crasnoscioc_nicolae`

---

## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.pytest.org/
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/

