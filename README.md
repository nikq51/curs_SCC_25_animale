# Marmota
============================

## Cuprins
1. [Descriere aplicație](#descriere-aplicație)
2. [Versiune și status](#versiune-și-status)
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

**Marmota** este o aplicație web creată în Python, care folosește framework-ul Flask pentru a oferi funcționalitate server-side. Proiectul este realizat cu scopul de a demonstra aplicarea conceptelor DevOps: testare automată, analiză statică a codului și livrare prin containere Docker.

Fișierul central este `marmota.py`, iar proiectul este organizat pentru a permite testare rapidă, integrare continuă și ușurință în dezvoltare colaborativă.

---

## Versiune și status
**v1.0 – prototip funcțional stabil**
- Implementare inițială terminată
- Cod verificat și testat
- Suport complet pentru CI/CD și containerizare

---

## Configurare și rulare

### 1. Activare mediu virtual și instalare pachete

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Rulare aplicație local

```bash
python3 marmota.py
```

Accesează aplicația la:
📍 `http://127.0.0.1:5000/`

---

## Testare

### 1. Testare unitară

```bash
python3 -m unittest app.test.test_marmota
```

Testele sunt scrise pentru a verifica răspunsurile aplicației și pot fi extinse ușor.

---

## Verificare calitate cod cu pylint

```bash
pylint marmota.py || true
```

Se verifică conformitatea codului cu standardele PEP8 și bune practici.

---

## DevOps – CI/CD

### Pipeline Jenkins

Fișierul `Jenkinsfile` gestionează următoarele etape:
- Creare mediu virtual
- Instalare pachete
- Analiză statică a codului cu `pylint`
- Testare automată cu `unittest`
- Build Docker + rulare container

Această integrare asigură livrare continuă și validare automată la fiecare commit.

---

## Containerizare

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "marmota.py"]
```

### Comenzi utile:

```bash
docker build -t marmota:v1 .
docker run -d -p 8020:5000 marmota:v1
```

Aplicația va fi accesibilă la `http://localhost:8020`.

---

## Stadiu dezvoltare branch

### Funcționalitate implementată:
- Server Flask funcțional în `marmota.py`
- Integrare completă cu Jenkins și Docker
- Testare automată funcțională

### Stadiul curent:
✅ Complet funcțional și testat local și în CI

### Testare:
- `unittest` validat
- `pylint` integrat în pipeline
- Docker funcțional local

### Integrare:
- Pull Request deschis pentru integrare în branch-ul principal

---

## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/
