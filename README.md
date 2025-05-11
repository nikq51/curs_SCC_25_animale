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

## Cuprins
1. Descriere aplicație
2. Versiune și status
   1. Probleme cunoscute
3. Configurare și rulare
4. Testare
5. Verificare calitate cod cu pylint
6. DevOps – CI/CD
   1. Pipeline Jenkins
7. Containerizare
8. Stadiu dezvoltare branch
9. Bibliografie


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

- Structura proiectului
- Descriere fișiere
- Utilizare
- Pipeline Jenkins
- Git Workflow
- Testare


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

## Cuprins

1. Descriere aplicație
2. Descriere versiune
3. Configurare
4. Exemple pagini web
5. Testare cu pytest
6. Verificare statică cu pylint
7. Bibliografie


## Descriere aplicație

Aplicația puma.py este o aplicație web simplă, scrisă în Python cu framework-ul Flask. Aceasta oferă o experiență interactivă în lumea pumei — un animal sălbatic elegant și agil.

Utilizatorul poate naviga prin mai multe rute web care oferă:
- descrierea pumei,
- culoarea blănii,
- locurile în care trăiește.

Aplicația este structurată modular:
- logica auxiliară este în app/lib/helper.py,
- testele unitare sunt în app/tests/.

Poate fi rulată în Docker și integrată într-un pipeline Jenkins.


## Descriere versiune
### v1.0 – prima versiune

* Ruta principală / – [http://127.0.0.1:5001](http://127.0.0.1:5001)
* Rute adiționale:
  * /puma – pagina principală cu imagine și butoane
  * /puma/descriere – descriere generală
  * /puma/culoare – detalii despre blană
  * /puma/descriere/locatii – regiuni geografice unde trăiește


## Configurare

Aplicația rulează într-un mediu virtual Python:

bash
python3 -m venv .venv             # creează mediu virtual
source .venv/bin/activate         # activează venv (Linux/macOS)
.venv\Scripts\activate.bat      # pentru Windows (cmd)

pip install -r quickrequirements.txt   # instalează dependențele
python puma.py                         # pornește serverul Flask


Serverul pornește la: http://127.0.0.1:5001


## Exemple pagini web

### Pagina principală /

Afișează mesaj de întâmpinare și un buton către lumea pumei.

### Pagina /puma

Prezintă imaginea pumei și două butoane:
- Descriere
- Culoare

### Pagina /puma/descriere

Text cu informații generale despre puma și un buton pentru locurile unde trăiește.

### Pagina /puma/culoare

Detalii despre culoarea blănii pumei și link de întoarcere.

### Pagina /puma/descriere/locatii

Listă cu regiuni geografice: Munții Anzi, Stâncoși, America Centrală etc.


## Testare cu pytest

Testele sunt plasate în app/tests/ și includ:
- Teste pentru funcțiile din app/lib/helper.py
- Teste pentru rutele definite în puma.py

bash
pytest app/tests



## Verificare statică cu pylint

Pachetul pylint verifică stilul și posibile probleme în codul Python.

bash
pylint puma.py app/lib/*.py app/tests/*.py


Notă: problemele găsite nu opresc execuția pipeline-ului.


## Bibliografie

* https://github.com/crchende/sysinfo
* https://www.jenkins.io/
* https://docs.docker.com/
* https://flask.palletsprojects.com/

---

# Crasnoșcioc Nicolae: manul

---

# Curiman Teodor: containerizare

## 1. Asigură-te că ai instalate următoarele:

- **Python 3.10+**
- **Docker**
- **Git**
- **venv** pentru un mediu virtual Python


## 2. Clonează proiectul

```bash
git clone --branch main_veverita https://github.com/TeodorCuriman/curs_SCC_25_veverita.git
cd curs_SCC_25_veverita
```



## 3. Rulează aplicația local cu Docker

### Build imaginea:

```bash
docker build -t veverita_app .
```

### Oprește orice instanță anterioară (dacă există):

```bash
docker stop veverita_container || true
docker rm veverita_container || true
```

###  Pornește aplicația:

```bash
docker run -d -p 5000:5000 --name veverita_container veverita_app
```


## 4. Deschide aplicația în browser:

- http://localhost:5000/veverita  
  sau  
- http://127.0.0.1:5000/veverita


## Despre proiect

Aplicația **Veverița App** din cadrul proiectului **SCC 2025** (student **[Numele tău]**, grupa **[Grupa ta]**) demonstrează un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă.


## Structura aplicației

### Biblioteca de funcții (`app/lib/biblioteca_animale.py`)

- `culoare_veverita()` – oferă o descriere a culorii blănii veveriței.
- `descriere_veverita()` – descriere generală a comportamentului veveriței.


### Server Flask (`app/main.py`)

Serverul definește rutele:

- `/veverita` – pagină principală cu linkuri.
- `/culoare_veverita` – afișează rezultatul `culoare_veverita()`.
- `/descriere_veverita` – afișează rezultatul `descriere_veverita()`.

Folosește `render_template_string` pentru HTML minimalist.


## Testare automată cu `pytest`

Teste definite în `tests/test_biblioteca_animale.py`:

- Verifică dacă `culoare_veverita()` returnează o culoare validă.
- Verifică dacă `descriere_veverita()` returnează un șir de caractere suficient de lung.

### Pentru a rula testele:

```bash
# Din rădăcina proiectului
PYTHONPATH=$(pwd) pytest
```


##  Containerizare Docker

Aplicația este containerizată folosind `Dockerfile`, bazat pe imaginea `python:3.12-slim`.

### Build manual:

```bash
docker build -t veverita_app .
```

### Rulează aplicația:

```bash
docker run -d -p 5000:5000 --name veverita_container veverita_app
```


## Automatizare CI/CD cu Jenkins

Proiectul include un `Jenkinsfile` cu etape declarative:

- **Checkout** – extragerea codului din `main_veverita`
- **Install** – instalarea dependențelor
- **Test** – rulare automată a testelor
- **Build Docker Image** – opțional, construire imagine Docker

Pipeline-ul se declanșează automat la fiecare `push`.


##  Concluzie

Proiectul **Veverița App** ilustrează un ciclu complet DevOps pentru o aplicație Python:

- Cod curat, modular
- Testare automată cu `pytest`
- Containerizare cu Docker
- Automatizare CI/CD cu Jenkins

---

# Drăgan Marina-Georgiana: urs


## Aplicație Flask – Urs

Aceasta este o aplicație web scrisă în Python folosind Flask, care oferă informații despre animalul urs. Aplicația este containerizată cu Docker și folosește Jenkins pentru rulare automată.

## Funcționalitate

Aplicația oferă următoarele rute:

- `/` – Pagina principală cu titlul temei și butoane de navigare
- `/urs` – Informații generale despre urs
- `/urs/alimentatie` – Informații despre alimentația ursului
- `/urs/specii` – Informații despre specii de urși

## Structura proiectului

```
curs_SCC_25_animale/
├── animale.py                 # Aplicația principală Flask
├── Dockerfile                # Fișier pentru containerizare
├── Jenkinsfile               # Pipeline pentru Jenkins
└── app/
    ├── lib/
    │   ├── info_general.py   # Funcții pentru homepage și /urs
    │   ├── alimentatie.py    # Funcție pentru alimentație
    │   └── specii.py         # Funcție pentru specii
    └── tests/
        └── test_caracteristici.py   # Teste simple
```

## Rulare aplicație

### Cu Docker

#### Build imagine

```bash
docker build -t aplicatie-urs .
```

#### Rulare container

```bash
docker run -p 9090:9090 --name urs_container aplicatie-urs
```

Aplicația poate fi accesată la: http://localhost:9090

## Jenkins

Fișierul Jenkinsfile automatizează următoarele etape:

1. Construirea imaginii Docker
2. Rularea testelor definite
3. Curățarea oricărui container existent
4. Pornirea aplicației într-un container nou

## Testare

Testele validează funcțiile implementate în fișierele din `lib` și compară rezultatele cu textele așteptate:

```bash
python3 -m app.tests.test_caracteristici
```

Rezultatele sunt afișate în consolă ca: `CORECT` sau `GREȘIT`.

---

# Dumitrescu Robert-Cristian: caine

---

# Ioana Crina-Maria: pisica

## Cuprins

1. Descriere aplicatie
2. Descriere versiune
3. Configurare
4. Exemple pagina web
5. Testare cu pytest
6. Verificare statica. pylint
7. Bibliografie

# Descriere aplicatie

Aplicatia pisica.py este o aplicatie web simpla scrisa in Python folosind framework-ul Flask, care simuleaza o mica aventura interactiva in lumea pisicilor. Utilizatorul poate naviga prin pagini HTML stilizate ce afiseaza informatii despre o pisica, precum descrierea, culoarea si nume amuzante.

Aplicatia este modularizata si organizata in foldere app/lib, app/tests, oferind si o componenta de testare unitara cu pytest, dar si verificare statica a codului cu pylint.

Aplicatia poate fi containerizata cu Docker si integrata in pipeline-uri Jenkins pentru testare si build automat.

# Descriere versiune
# v1.0 - prima versiune

* ruta principala '/' - [http://127.0.0.1:5050](http://127.0.0.1:5050)
* rute aditionale:
  * '/pisica' - pagina "home" cu poza si butoane
  * '/pisica/descriere' - descrierea pisicii
  * '/pisica/culoare' - culoarea pisicii
  * '/pisica/descriere/nume' - lista cu nume de pisici

# Configurare

Aplicatia se bazeaza pe un mediu virtual si necesita instalarea dependintelor:

python3 -m venv .venv                  -> creeaza un mediu virtual Python in folderul .venv

source .venv/bin/activate              -> activeaza mediul virtual

pip install -r quickrequirements.txt   -> instaleaza toate bibliotecile din fisierul quickrequirements.txt

python pisica.py                       -> porneste aplicatia pisica.py

Serverul porneste pe IP: 127.0.0.1 si port 5050. Acces server din browser: http://127.0.0.1:5050

# Exemple pagina web

## Pagina principala

* Afișează un mesaj de bun venit și un buton de acces către pagina "pisica".

## Pagina "pisica"

* Afiseaza două butoane catre alte rute: Descriere și Culoare.

## Pagina descriere

* Afișează un text cu descrierea pisicii și un buton pentru afișarea unor nume simpatice.

## Pagina culoare

* Afișează informații despre culoarea pisicii și un link de întoarcere la pagina principala.

## Pagina nume

* Afișează lista de nume amuzante pentru pisici.

# Testare cu pytest

Testele sunt plasate in app/tests/ si verifica:

* Functionalitatea functiilor helper (din app/lib/helper.py)
* Raspunsul generat de rutele principale (/, /pisica, etc.)

# Verificare statica cu pylint

-> pylint - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
-> in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

pylint pisica.py app/lib/*.py app/tests/*.py

# Bibliografie

* https://github.com/crchende/sysinfo
* https://www.jenkins.io/
* https://docs.docker.com/

---

# Ion Filip-Viorel: alpaca

## Tutorial
1. Asigură-te că Make este instalat pe sistem (ex. sudo apt install make pe Ubuntu).

2. Ruleaza intr-un terminal de linux urmatoarele 3 comenzi:

git clone --branch main_ion_filip https://github.com/nikq51/curs_SCC_25_animale.git

cd curs_SCC_25_animale

make all

3.  Deschide in browser 
http://localhost:5000/alpaca
-------------sau-----------------
http://127.0.0.1:5000/alpaca

## Despre proiect

Aplicația Alpaca App din cadrul proiectului SCC 2025 (student Ion Filip-Viorel, grupa 441D) își propune să demonstreze un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă. Principalii pași parcurși sunt:

   Biblioteca de funcții pentru Alpaca

        În app/lib/biblioteca_animale.py am definit două funcții:

            culoare_alpaca(), care returnează o descriere a culorii lânii alpaca

            descriere_alpaca(), care oferă informații generale despre animal
	    
Server Flask

        În app/main.py am creat un server Flask cu trei rute:

            /alpaca – pagina principală, cu linkuri către subpagini

            /culoare_alpaca – afișează rezultatul lui culoare_alpaca()

            /descriere_alpaca – afișează rezultatul lui descriere_alpaca()

        Am folosit render_template_string pentru a genera rapid un meniu simplu cu hyperlink-uri.

   Teste automatizate cu pytest

        În tests/test_biblioteca_animale.py am scris teste care:

            verifică că culoare_alpaca() returnează un șir de caractere ce conține o culoare

            verifică că descriere_alpaca() returnează un șir de minim 10 caractere

   Rulez testele local cu:

    PYTHONPATH=$(pwd) pytest

Containerizare Docker

    Fișierul Dockerfile definește o imagine pe bază de python:3.12-slim, copiază codul, instalează dependențele din requirements.txt și pornește serverul Flask.

    Local, imaginea e construită cu:

	docker build -t alpaca_app .

	Și rulează astfel:

    docker run -p 5000:5000 alpaca_app

Automatizare CI/CD cu Jenkins

    Am definit un Jenkinsfile în modul declarativ, cu etape de:

        Checkout – preia codul din branch-ul main_ion_filip

        Install – pip install -r requirements.txt

        Test – pytest --maxfail=1 --disable-warnings -q

        Build Docker Image (opțional) – docker build -t alpaca_app .

    Jenkins rulează pipeline-ul la fiecare push, asigurându-se că codul e testat și containerul poate fi construit.

Makefile

	Un makefile este practic un script ce poate fi rulat cu "make" pentru a compila un executabil binar final.

    În rădăcina repo-ului am adăugat un Makefile cu ținte:

        make build – construiește imaginea Docker

        make run – pornește containerul (după ce oprește oricare instanță anterioară)

        make stop – oprește și șterge containerul

        make all – rulează build și run într-o singură comandă

    Astfel, utilizatorii pot porni tot fluxul local cu:
    
        make all

În ansamblu, proiectul demonstrează întregul ciclu de viață al unei aplicații: de la scrierea codului și testare, la containerizare și automatizare CI/CD, toate acestea fiind bine documentate în README pentru ușurința utilizării și prezentării.


---

# Ionescu Razvan: marmota

## Cuprins
1. Descriere aplicație
2. Versiune și status
3. Configurare și rulare
4. Testare
5. Verificare calitate cod cu pylint
6. DevOps – CI/CD
   1. Pipeline Jenkins
7. Containerizare
8. Stadiu dezvoltare branch
9. Bibliografie


## Descriere aplicație

**Marmota** este o aplicație web creată în Python, care folosește framework-ul Flask pentru a oferi funcționalitate server-side. Proiectul este realizat cu scopul de a demonstra aplicarea conceptelor DevOps: testare automată, analiză statică a codului și livrare prin containere Docker.

Fișierul central este `marmota.py`, iar proiectul este organizat pentru a permite testare rapidă, integrare continuă și ușurință în dezvoltare colaborativă.


## Versiune și status
**v1.0 – prototip funcțional stabil**
- Implementare inițială terminată
- Cod verificat și testat
- Suport complet pentru CI/CD și containerizare


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


## Testare

### 1. Testare unitară

```bash
python3 -m unittest app.test.test_marmota
```

Testele sunt scrise pentru a verifica răspunsurile aplicației și pot fi extinse ușor.


## Verificare calitate cod cu pylint

```bash
pylint marmota.py || true
```

Se verifică conformitatea codului cu standardele PEP8 și bune practici.


## DevOps – CI/CD

### Pipeline Jenkins

Fișierul `Jenkinsfile` gestionează următoarele etape:
- Creare mediu virtual
- Instalare pachete
- Analiză statică a codului cu `pylint`
- Testare automată cu `unittest`
- Build Docker + rulare container

Această integrare asigură livrare continuă și validare automată la fiecare commit.


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


## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.python.org/3/library/unittest.html
- https://pylint.pycqa.org/
- https://www.jenkins.io/doc/book/pipeline/
- https://docs.docker.com/

---

# Ionescu Ștefania: cal

---

# Ivașcu Alexia-Ioana: tigru

## Cuprins

1. Descriere aplicație
2. Structură directoare
3. Rularea aplicației
4. Testare unitară
5. Verificare cod cu pylint
6. Containerizare Docker
7. CI/CD cu Jenkins
8. Bibliografie


## Descriere aplicație

Această aplicație a fost realizată ca temă în cadrul cursului **Servicii Cloud și Containerizare (SCC)** – 2025.

Aplicația este scrisă în Python și oferă o interfață simplă prin Flask, unde sunt prezentate informații despre animalul ales: **Tigrul**.  
Utilizatorul poate accesa din browser descrierea, habitatul și alimentația tigrului.

Aplicația este testabilă, containerizată cu Docker și automatizată printr-un pipeline Jenkins.


## Structură directoare

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


## Rularea aplicației

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


## Testare unitară

Comandă de rulare locală:

```bash
PYTHONPATH=$PWD python3 -m unittest discover -s app/tests -p "test_*.py"
```


## Verificare statică cu pylint

```bash
pylint app/lib/helper.py
pylint app/tests/test_tigru.py
```


## Containerizare Docker

### Build:

```bash
docker build -t tigru-app .
```

### Rulare:

```bash
docker run -p 5000:5000 tigru-app
```


## CI/CD cu Jenkins

Pipeline-ul automat include:

* Clonare repository
* Instalare dependențe
* Rulare teste unitar
* Build imagine Docker

![jenkins](https://upload.wikimedia.org/wikipedia/commons/e/e9/Jenkins_logo.svg)


## Bibliografie

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

---

# Ladiu Andrei-Cătălin: lup

## Descriere

**Lup App** este un proiect din cadrul cursului SCC 2025, care demonstrează un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă, folosind Python, Flask, Docker, pytest și Jenkins.

### Funcționalități

- **Culoarea veveriței**: Afișează o descriere a culorii blănii veveriței.
- **Comportament Lup**: Oferă o descriere generală a comportamentului veveriței.

## Tehnologii

- **Python 3.10+**
- **Flask**
- **Docker**
- **pytest** pentru testare automată
- **Jenkins** pentru CI/CD

## Pași de instalare

### 1. Asigură-te că ai instalate următoarele:

- **Python 3.10+**
- **Docker**
- **Git**
- **venv** pentru un mediu virtual Python

### 2. Clonează proiectul

```bash
git clone --branch main_veverita https://github.com/TeodorCuriman/curs_SCC_25_veverita.git
cd curs_SCC_25_veverita
```

### 3. Rulează aplicația local cu Docker

#### Build imaginea:

```bash
docker build -t veverita_app .
```

#### Oprește orice instanță anterioară (dacă există):

```bash
docker stop veverita_container || true
docker rm veverita_container || true
```

#### Pornește aplicația:

```bash
docker run -d -p 5000:5000 --name veverita_container veverita_app
```

### 4. Deschide aplicația în browser:

Accesează aplicația în browser la următoarele linkuri:

- [http://localhost:5000/veverita](http://localhost:5000/veverita)  
- [http://127.0.0.1:5000/veverita](http://127.0.0.1:5000/veverita)

## Structura aplicației

### Biblioteca de funcții (app/lib/biblioteca_animale.py)

- **culoare_veverita()** – oferă o descriere a culorii blănii veveriței.
- **descriere_veverita()** – descriere generală a comportamentului veveriței.

### Server Flask (app/main.py)

Serverul definește rutele:

- **/veverita** – pagină principală cu linkuri.
- **/culoare_veverita** – afișează rezultatul `culoare_veverita()`.
- **/descriere_veverita** – afișează rezultatul `descriere_veverita()`.

Folosește `render_template_string` pentru HTML minimalist.

## Testare automată cu pytest

Teste definite în **tests/test_biblioteca_animale.py**:

- Verifică dacă `culoare_veverita()` returnează o culoare validă.
- Verifică dacă `descriere_veverita()` returnează un șir de caractere suficient de lung.

### Pentru a rula testele:

```bash
# Din rădăcina proiectului
PYTHONPATH=$(pwd) pytest
```

## Containerizare Docker

Aplicația este containerizată folosind Dockerfile, bazat pe imaginea **python:3.12-slim**.

### Build manual:

```bash
docker build -t veverita_app .
```

### Rulează aplicația:

```bash
docker run -d -p 5000:5000 --name veverita_container veverita_app
```

## Automatizare CI/CD cu Jenkins

Proiectul include un **Jenkinsfile** cu etape declarative:

- **Checkout** – extragerea codului din `main_veverita`
- **Install** – instalarea dependențelor
- **Test** – rulare automată a testelor
- **Build Docker Image** – opțional, construire imagine Docker

Pipeline-ul se declanșează automat la fiecare push.


---

# Manea Claudiu-Florin: bizon

## Proiect: Bizon 🦬

Aplicație web dezvoltată în Python folosind Flask, care oferă informații despre bizon (descriere și habitat). Include testare unitară, analiză statică a codului și pipeline de livrare continuă cu Jenkins și Docker.


## 📁 Structura proiectului

- `Bizon.py` – Aplicația principală Flask care definește rutele web.
- `testare.py` – Teste unitare pentru funcțiile `get_descriere()` și `get_habitat()`.
- `Dockerfile.txt` – Fișier de configurare pentru containerizarea aplicației.
- `Jenkinsfile.txt` – Definirea pipeline-ului CI/CD.
- `app/lib/descriere.py` – Funcție care oferă descrierea bizonului.
- `app/lib/habitat.py` – Funcție care returnează informații despre habitatul bizonului.
- `quickrequirements.txt` sau `requirements.txt` – Lista pachetelor necesare.


## 🚀 Rulare locală

### 1. Instalare dependințe

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


2. Pornire aplicație
python Bizon.py


3.Utilizare Docker
docker build -t bizon .
docker run -p 5000:5000 bizon

4.Testare unitară
python -m unittest discover -s test -p "testare.py"

5. Jenkins CI/CD
-Jenkinsfile-ul definește următoarele etape:
-Configurare mediu virtual și instalare dependințe.
-Analiză cod cu pylint.
-Rulare teste unitare.
-Construire imagine Docker și creare container cu versiune incrementată (bizon:v${BUILD_NUMBER}).
```

---

# Manea Mihaita-Cristian: arici

## Aplicație Web Flask – Arici

Aceasta este o aplicație web construită cu Flask, în care sunt prezentate informații despre arici:
- Pagini descriptive: Despre, Curiozități, Zgomot, Emoji, Detalii, Prădători
- Navigare ușoară prin meniul principal

## Structură
- `animale.py`: punctul de pornire al aplicației
- `lib/`: conține funcțiile logice pentru fiecare pagină
- `tests/`: conține testele unitare pentru funcții

## Testare
- Teste scrise cu `pytest`
- Calitatea codului verificată cu `pylint`
- Executate automat în Jenkins

## Rulare locală
```bash
source app/activeaza_venv
python3 animale.py
```

---

# Mirea Catalin-Gabriel: raton

## 📑 Cuprins
1. Descriere
2. Instalare si lansare
3. Testare
4. Containerizare Docker
5. CI cu Jenkins

## 🐭 Raton

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
docker build -t raton:v1 .
docker run -d -p 5000:5000 --name app raton:v1
```
## CI cu Jenkins

`Jenkinsfile` definește etapele de build, testare și livrare:

- Setup mediu virtual
- Instalare dependințe
- Analiză cu pylint
- Testare automată
- Build și rulare imagine Docker


---

# Panait Denis-Valentin: vulpe

## 📑 Cuprins
1. Descriere
2. Instalare si lansare
3. Testare
4. Containerizare Docker
5. CI cu Jenkins

## 🦊 Vulpe

Vulpe este o aplicație web simplă, construită cu [Flask] în Python. Scopul ei este să demonstreze cum poți construi rapid o aplicație web ușor de testat, containerizat și integrat într-un flux CI/CD cu Jenkins.

## 🚀 Ce face

- Servește o interfață web de bază
- E pregătită pentru testare automată
- Se rulează în containere Docker
- Integrare ușoară cu Jenkins pentru CI

## 🗂 Structură simplă

- `vulpe.py` – fișierul principal al aplicației
- `Dockerfile` – pentru rulare în container
- `tests/` – loc pentru testele automate

## Instalare si lansare

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
python3 vulpe.py
```

## Testare


Testele sunt scrise în `app/test/testare.py` și pot fi rulate cu:

```bash
python3 -m unittest app.test.testare
```
## Docker

```bash
docker build -t vulpe:v1 .
docker run -d -p 5000:5000 --name app vulpe:v1
```
## CI cu Jenkins

`Jenkinsfile` definește etapele de build, testare și livrare:

- Setup mediu virtual
- Instalare dependințe
- Analiză cu pylint
- Testare automată
- Build și rulare imagine Docker


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
