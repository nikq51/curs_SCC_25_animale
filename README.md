# Tema: Animale
============================

## Cuprins
1. [Baranga Andreea-Maria: zebra](#Baranga_Andreea_Maria:_zebra)
2. [Basarab Elena Florentina: leopard](#leopard)
3. [Bratu Andreea-Ioana: pantera](#pantera)
4. [Busuioc Nicu-Lucian: capibara](#capibara)
5. [Calota Andrei Cosmin: leu](#leu)
6. [Chirtoaca Andreea: panda](#panda)
7. [Ciobanu Christiana-Andreea: puma](#puma)
8. [Crasnoșcioc Nicolae: manul](#manul)
9. [Curiman Teodor: ](#containerizare)
10. [Drăgan Marina-Georgiana: urs](#uss)
11. [Dumitrescu Robert-Cristian: caine](#caine)
12. [Ioana Crina-Maria: pisica](#pisica)
13. [Ion Filip-Viorel: alpaca](#alpaca)
14. [Ionescu Razvan: marmota](#marmota)
15. [Ionescu Ștefania: cal](#cal)
16. [Ivașcu Alexia-Ioana: tigru](#tigru)
17. [Ladiu Andrei-Cătălin: lup](#lup)
18. [Manea Claudiu-Florin: bizon](#bizon)
19. [Manea Mihaita-Cristian: arici](#arici)
20. [Mirea Catalin-Gabriel: raton](#raton)
21. [Panait Denis-Valentin: vulpe](#vulpe)
22. [Petrache Andrei-Nicolae: delfin](#delfin)
23. [Prioteasa Ioana: vidra](#vidra)
24. [Stan Maria: lemur](#lemur)
25. [Tudor Tudor: vultur](#vultur)
26. [Zamfir Alin-George: nevastuica](#nevastuica)
27. [Zamirca Minodora Adriana: koala](#koala)

---

# Baranga Andreea-Maria: zebra

---

# Baranga Andreea-Maria: zebra

---

# Baranga Andreea-Maria: zebra

## Descriere aplicație

**Capibara** este o aplicație dezvoltată în Python, bazată pe Flask, care servește drept exemplu de aplicație web simplă, cu integrare completă în DevOps. Este gândită pentru a permite testare automată, analiză a calității codului și livrare rapidă prin containerizare cu Docker și CI în Jenkins.

Fișierul principal este `capibara.py`, iar aplicația este pregătită pentru dezvoltare colaborativă și scalabilă.

---

## Versiune și status
**v1.0 – aplicație minim viabilă (MVP)**
- Toate componentele esențiale funcționează
- Codul este testat și analizat automat
- Integrare completă în pipeline

### Probleme cunoscute
- Interfață web minimă, fără HTML sau CSS
- Necesită extindere pentru funcționalități suplimentare

---

## Configurare și rulare

### 1. Creare mediu virtual și instalare pachete

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Lansare aplicație

```bash
python3 capibara.py
```

Aplicația pornește pe adresa:
📍 `http://127.0.0.1:5000/`

---

## Testare

### 1. Executare teste

Testele sunt scrise în `app/test/testare.py` și pot fi rulate cu:

```bash
python3 -m unittest app.test.testare
```

Testele validează funcțiile principale ale aplicației.

---

## Verificare calitate cod cu pylint

```bash
pylint capibara.py || true
```

Analiza codului este parte din pipeline și verifică respectarea convențiilor Python (PEP8).

---

## DevOps – CI/CD

### Pipeline Jenkins

`Jenkinsfile` definește etapele de build, testare și livrare:

- Setup mediu virtual
- Instalare dependințe
- Analiză cu pylint
- Testare automată
- Build și rulare imagine Docker

Acest pipeline rulează automat la fiecare modificare în branch.

---

## Containerizare

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "capibara.py"]
```

### Comenzi utile:

```bash
docker build -t capibara:v1 .
docker run -d -p 8022:5000 capibara:v1
```

Acces aplicație: `http://localhost:8022`

---

## Stadiu dezvoltare branch

### Implementare:
- Server Flask de bază în `capibara.py`
- CI/CD și containerizare validate

### Testare efectuată:
- Test unitar + static check
- Build Docker testat în Jenkins

### Integrare:
- Branch activ: `devel_capibara_...`
- Pull request deschis pentru `main`

---

## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/
