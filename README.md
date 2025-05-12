
# Lup App

## Descriere

**Lup App** este un proiect din cadrul cursului SCC 2025, care demonstrează un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă, folosind Python, Flask, Docker, pytest și Jenkins.

### Funcționalități

- **Culoarea lup**: Afișează o descriere a culorii blănii lup.
- **Comportament Lup**: Oferă o descriere generală a comportamentului lup.

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
git clone --branch main_lup https://github.com/CataLadiu/curs_SCC_25_lup.git
cd curs_SCC_25_lup
```

### 3. Rulează aplicația local cu Docker

#### Build imaginea:

```bash
docker build -t lup_app .
```

#### Oprește orice instanță anterioară (dacă există):

```bash
docker stop lup_container || true
docker rm lup_container || true
```

#### Pornește aplicația:

```bash
docker run -d -p 5000:5000 --name lup_container lup_app
```

### 4. Deschide aplicația în browser:

Accesează aplicația în browser la următoarele linkuri:

- [http://localhost:5000/lup](http://localhost:5000/lup)  
- [http://127.0.0.1:5000/lup](http://127.0.0.1:5000/lup)

## Structura aplicației

### Biblioteca de funcții (app/lib/biblioteca_animale.py)

- **culoare_lup()** – oferă o descriere a culorii blănii lup.
- **descriere_lup()** – descriere generală a comportamentului lup.

### Server Flask (app/main.py)

Serverul definește rutele:

- **/lup** – pagină principală cu linkuri.
- **/culoare_lup** – afișează rezultatul `culoare_lup()`.
- **/descriere_lup** – afișează rezultatul `descriere_lup()`.

Folosește `render_template_string` pentru HTML minimalist.

## Testare automată cu pytest

Teste definite în **tests/test_biblioteca_animale.py**:

- Verifică dacă `culoare_lup()` returnează o culoare validă.
- Verifică dacă `descriere_lup()` returnează un șir de caractere suficient de lung.

### Pentru a rula testele:

```bash
# Din rădăcina proiectului
PYTHONPATH=$(pwd) pytest
```

## Containerizare Docker

Aplicația este containerizată folosind Dockerfile, bazat pe imaginea **python:3.12-slim**.

### Build manual:

```bash
docker build -t lup_app .
```

### Rulează aplicația:

```bash
docker run -d -p 5000:5000 --name lup_container lup_app
```

## Automatizare CI/CD cu Jenkins

Proiectul include un **Jenkinsfile** cu etape declarative:

- **Checkout** – extragerea codului din `main_lup`
- **Install** – instalarea dependențelor
- **Test** – rulare automată a testelor
- **Build Docker Image** – opțional, construire imagine Docker

Pipeline-ul se declanșează automat la fiecare push.
