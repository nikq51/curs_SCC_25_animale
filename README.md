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


## Testare

### 1. Executare teste

Testele sunt scrise în `app/test/testare.py` și pot fi rulate cu:

```bash
python3 -m unittest app.test.testare
```

Testele validează funcțiile principale ale aplicației.


## Verificare calitate cod cu pylint

```bash
pylint capibara.py || true
```

Analiza codului este parte din pipeline și verifică respectarea convențiilor Python (PEP8).


## DevOps – CI/CD

### Pipeline Jenkins

`Jenkinsfile` definește etapele de build, testare și livrare:

- Setup mediu virtual
- Instalare dependințe
- Analiză cu pylint
- Testare automată
- Build și rulare imagine Docker

Acest pipeline rulează automat la fiecare modificare în branch.


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


## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/

---

# Calota Andrei Cosmin: leu

## Aplicație Flask – ANIMALE (Leul)

Aceasta este o aplicație web simplă scrisă în Python folosind Flask, care prezintă informații despre leu: culoare și habitat. Proiectul este containerizat cu Docker și include un pipeline Jenkins pentru build, testare și rulare automată.


## Structura Proiectului

```
curs_SCC_25_animale/
├── animale.py                  # Punctul de intrare al aplicației Flask
├── app/
│   ├── lib/
│   │   ├── culoare.py          # Funcție ce returnează culoarea leului
│   │   └── habitat.py          # Funcție ce returnează habitatul leului
│   └── tests/
│       └── test_caracteristici.py  # Teste pentru culoare și habitat
├── Dockerfile                  # Dockerfile pentru containerizare
├── Jenkinsfile                 # Pipeline Jenkins pentru CI/CD
├── LICENSE                     
└── README.md                   # Documentația proiectului
```


## Rulare Locală cu Docker

### 1. Clonare repository

```bash
git clone https://github.com/nikq51/curs_SCC_25_animale.git
cd curs_SCC_25_animale
```

### 2. Build imagine Docker

```bash
docker build -t aplicatie-leu .
```

### 3. Rulează containerul

```bash
docker run -d -p 7070:7070 --name leut_container aplicatie-leu
```

### 4. Accesează aplicația

Deschide în browser: [http://localhost:7070](http://localhost:7070)


## Rute Disponibile

- `/` – Pagina principală
- `/leu` – Informație generală despre leu
- `/leu/culoare` – Culoarea tipică a leului
- `/leu/habitat` – Habitatul natural al leului


## Testare

Rulează testele local cu:

```bash
python3 -m app.tests.test_caracteristici
```

Testele verifică valorile returnate de funcțiile `get_culoare()` și `get_habitat()`.


## Jenkins Pipeline

Fișierul `Jenkinsfile` definește un pipeline automat cu următoarele etape:

- Listare directoare
- Build Docker
- Rulare teste
- Curățare container anterior
- Rulare container nou

---

# Chirtoaca Andreea: panda

## Descriere

Acest proiect este o aplicație web simplă realizată în Flask, care oferă informații despre panda: culoare și alimentație.  
Proiectul este realizat de **Chirtoacă Andreea**, grupa 441D.

Aplicația conține:
- o interfață web cu rute dedicate pentru panda
- testare automată
- integrare Docker
- pipeline de CI cu Jenkins


## Cuprins

- [Structura proiectului]
- [Descriere fișiere]
- [Utilizare]
- [Pipeline Jenkins]
- [Git Workflow]
- [Testare]


## Structura proiectului

```
.
├── animale.py
├── app
│   ├── lib
│   │   ├── alimentatie.py
│   │   ├── culoare.py
│   └── tests
│       └── test_animale.py
├── Dockerfile
├── Jenkinsfile
├── LICENSE
└── README.md
```


## Descriere fișiere

- `animale.py` – Aplicația principală Flask, definește rutele web.
- `app/lib/alimentatie.py` – Conține funcția care returnează descrierea alimentației panda.
- `app/lib/culoare.py` – Conține funcția care returnează informații despre culoarea panda.
- `app/tests/test_animale.py` – Teste pentru funcțiile `get_alimentatie` și `get_culoare`.
- `Dockerfile` – Definește imaginea Docker pentru rularea aplicației Flask.
- `Jenkinsfile` – Definește pipeline-ul Jenkins (testare, build, rulare container).
- `LICENSE` – Licența proiectului.
- `README.md` – Documentația proiectului (acest fișier).


## Utilizare

### Rulare locală

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
python animale.py
```

Accesează aplicația în browser la: [http://localhost:5000](http://localhost:5000)


### Rulare în Docker

```bash
docker build -t app-panda .
docker run -d -p 5000:5000 --name app app-panda
```


## Pipeline Jenkins

Definit în `Jenkinsfile`. Include:

1. Listare directoare
2. Rulare teste
3. Build Docker image
4. Curățare și rulare container


## Git Workflow

Proiectul folosește două branch-uri:

- `main_chirtoaca_andreea` – versiunea stabilă
- `devel_chirtoaca_andreea` – dezvoltare activă

Fluxul de lucru:

1. Se lucrează pe `devel_chirtoaca_andreea`
2. Se testează și se face `commit + push`
3. Se face `merge` în `main_chirtoaca_andreea` după verificare


## Testare

Testele sunt definite în `app/tests/test_animale.py`.  
Verifică funcțiile:

- `get_alimentatie()` – trebuie să returneze alimentația corectă a panda
- `get_culoare()` – trebuie să returneze descrierea culorii panda

Rulare:

```bash
python app/tests/test_animale.py
```

---

# Ciobanu Christiana-Andreea: puma

---

# Crasnoșcioc Nicolae: manul

---

# Curiman Teodor: containerizare

---

# Drăgan Marina-Georgiana: urs

---

# Dumitrescu Robert-Cristian: caine

---

# Ioana Crina-Maria: pisica

---

# Ion Filip-Viorel: alpaca

---

# Ionescu Razvan: marmota

---

# Ionescu Ștefania: cal

---

# Ivașcu Alexia-Ioana: tigru

---

# Ladiu Andrei-Cătălin: lup

---

# Manea Claudiu-Florin: bizon

---

# Manea Mihaita-Cristian: arici

---

# Mirea Catalin-Gabriel: raton

---

# Panait Denis-Valentin: vulpe

---

# Petrache Andrei-Nicolae: delfin 

---

# Prioteasa Ioana: vidra

---

# Stan Maria: lemur

---

# Tudor Tudor: vultur

---

# Zamfir Alin-George: nevastuica

---

# Zamirca Minodora Adriana: koala
