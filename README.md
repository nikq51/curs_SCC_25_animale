# Tema: Animale
============================

## Cuprins

1. [Baranga Andreea-Maria: zebra](#baranga-andreea-maria-zebra)  
2. [Basarab Elena Florentina: leopard](#basarab-elena-florentina-leopard)  
3. [Bratu Andreea-Ioana: pantera](#bratu-andreea-ioana-pantera)  
4. [Busuioc Nicu-Lucian: capibara](#busuioc-nicu-lucian-capibara)  
5. [Calota Andrei Cosmin: leu](#calota-andrei-cosmin-leu)  
6. [Chirtoaca Andreea: panda](#chirtoaca-andreea-panda)  
7. [Ciobanu Christiana-Andreea: puma](#ciobanu-christiana-andreea-puma)  
8. [Crasnoșcioc Nicolae: manul](#crasnoscioc-nicolae-manul)  
9. [Curiman Teodor: containerizare](#curiman-teodor-containerizare)  
10. [Drăgan Marina-Georgiana: urs](#dragan-marina-georgiana-urs)  
11. [Dumitrescu Robert-Cristian: caine](#dumitrescu-robert-cristian-caine)  
12. [Ioana Crina-Maria: pisica](#ioana-crina-maria-pisica)  
13. [Ion Filip-Viorel: alpaca](#ion-filip-viorel-alpaca)  
14. [Ionescu Razvan: marmota](#ionescu-razvan-marmota)  
15. [Ionescu Ștefania: cal](#ionescu-stefania-cal)  
16. [Ivașcu Alexia-Ioana: tigru](#ivascu-alexia-ioana-tigru)  
17. [Ladiu Andrei-Cătălin: lup](#ladiu-andrei-catalin-lup)  
18. [Manea Claudiu-Florin: bizon](#manea-claudiu-florin-bizon)  
19. [Manea Mihaita-Cristian: arici](#manea-mihaita-cristian-arici)  
20. [Mirea Catalin-Gabriel: raton](#mirea-catalin-gabriel-raton)  
21. [Panait Denis-Valentin: vulpe](#panait-denis-valentin-vulpe)  
22. [Petrache Andrei-Nicolae: delfin](#petrache-andrei-nicolae-delfin)  
23. [Prioteasa Ioana: vidra](#prioteasa-ioana-vidra)  
24. [Stan Maria: lemur](#stan-maria-lemur)  
25. [Tudor Tudor: vultur](#tudor-tudor-vultur)  
26. [Zamfir Alin-George: nevastuica](#zamfir-alin-george-nevastuica)  
27. [Zamirca Minodora Adriana: koala](#zamirca-minodora-adriana-koala)  

---

# Baranga Andreea-Maria: zebra

---

# Basarab Elena Florentina: leopard

---

# Bratu Andreea-Ioana: pantera

---

# Busuioc Nicu-Lucian: capibara

## Descriere aplicație

**Capibara** este o aplicație dezvoltată în Python, bazată pe Flask, care servește drept exemplu de aplicație web simplă, cu integrare completă în DevOps. Este gândită pentru a permite testare automată, analiză a calității codului și livrare rapidă prin containerizare cu Docker și CI în Jenkins.

Fișierul principal este `capibara.py`, iar aplicația este pregătită pentru dezvoltare colaborativă și scalabilă.

## Versiune și status

**v1.0 – aplicație minim viabilă (MVP)**  
- Toate componentele esențiale funcționează  
- Codul este testat și analizat automat  
- Integrare completă în pipeline

### Probleme cunoscute

- Interfață web minimă, fără HTML sau CSS  
- Necesită extindere pentru funcționalități suplimentare

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

---

Calota Andrei Cosmin: leu

---

Chirtoaca Andreea: panda

---

Ciobanu Christiana-Andreea: puma

---

Crasnoșcioc Nicolae: manul

---

Curiman Teodor: containerizare

---

Drăgan Marina-Georgiana: urs

---

Dumitrescu Robert-Cristian: caine

---

Ioana Crina-Maria: pisica

---

Ion Filip-Viorel: alpaca

---

Ionescu Razvan: marmota

---

Ionescu Ștefania: cal

---

Ivașcu Alexia-Ioana: tigru

---

Ladiu Andrei-Cătălin: lup

---

Manea Claudiu-Florin: bizon

---

Manea Mihaita-Cristian: arici

---

Mirea Catalin-Gabriel: raton

---

Panait Denis-Valentin: vulpe

---

Petrache Andrei-Nicolae: delfin 

---

Prioteasa Ioana: vidra

---

Stan Maria: lemur

---

Tudor Tudor: vultur

---

Zamfir Alin-George: nevastuica

---

Zamirca Minodora Adriana: koala
