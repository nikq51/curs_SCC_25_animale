## 📑 Cuprins
1. [Descriere]
2. [Instalare si lansare]
3. [Testare]
4. [Containerizare Docker]
5. [CI cu Jenkins]

---
# 🐭 Raton

Raton este o aplicație web simplă, construită cu [Flask] în Python. Scopul ei este să demonstreze cum poți construi rapid o aplicație web ușor de testat, containerizat și integrat într-un flux CI/CD cu Jenkins.

## 🚀 Ce face

- Servește o interfață web de bază
- E pregătită pentru testare automată
- Se rulează în containere Docker
- Integrare ușoară cu Jenkins pentru CI

## 🗂 Structură simplă

- `raton.py` – fișierul principal al aplicației
- `Dockerfile` – pentru rulare în container
- `tests/` – loc pentru testele automate

## Instalare si lansare

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
python3 raton.py
```

## Testare


Testele sunt scrise în `app/test/testare.py` și pot fi rulate cu:

```bash
python3 -m unittest app.test.testare
```
## Docker

```bash
docker build -t app-panda .
docker run -d -p 5000:5000 --name app app-panda
```
## CI cu Jenkins

`Jenkinsfile` definește etapele de build, testare și livrare:

- Setup mediu virtual
- Instalare dependințe
- Analiză cu pylint
- Testare automată
- Build și rulare imagine Docker


---
