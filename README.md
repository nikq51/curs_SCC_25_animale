# Veverița App – Tutorial fără Makefile

## 1. Asigură-te că ai instalate următoarele:

- **Python 3.10+**
- **Docker**
- **Git**
- (opțional) **pipenv** sau **venv** pentru un mediu virtual Python

---

## 2. Clonează proiectul

```bash
git clone --branch main_veverita https://github.com/USERNAME/curs_SCC_25_veverita.git
cd curs_SCC_25_veverita
```

> Înlocuiește `USERNAME` cu numele tău de utilizator de GitHub dacă e cazul.

---

## 3. Rulează aplicația local cu Docker

### 🔨 Build imaginea:

```bash
docker build -t veverita_app .
```

### 🛑 Oprește orice instanță anterioară (dacă există):

```bash
docker stop veverita_container || true
docker rm veverita_container || true
```

### 🚀 Pornește aplicația:

```bash
docker run -d -p 5000:5000 --name veverita_container veverita_app
```

---

## 4. Deschide aplicația în browser:

- http://localhost:5000/veverita  
  sau  
- http://127.0.0.1:5000/veverita

---

# 📚 Despre proiect

Aplicația **Veverița App** din cadrul proiectului **SCC 2025** (student **[Numele tău]**, grupa **[Grupa ta]**) demonstrează un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă.

---

## Structura aplicației

### ✅ Biblioteca de funcții (`app/lib/biblioteca_animale.py`)

- `culoare_veverita()` – oferă o descriere a culorii blănii veveriței.
- `descriere_veverita()` – descriere generală a comportamentului veveriței.

---

### 🌐 Server Flask (`app/main.py`)

Serverul definește rutele:

- `/veverita` – pagină principală cu linkuri.
- `/culoare_veverita` – afișează rezultatul `culoare_veverita()`.
- `/descriere_veverita` – afișează rezultatul `descriere_veverita()`.

Folosește `render_template_string` pentru HTML minimalist.

---

## ✅ Testare automată cu `pytest`

Teste definite în `tests/test_biblioteca_animale.py`:

- Verifică dacă `culoare_veverita()` returnează o culoare validă.
- Verifică dacă `descriere_veverita()` returnează un șir de caractere suficient de lung.

### Pentru a rula testele:

```bash
# Din rădăcina proiectului
PYTHONPATH=$(pwd) pytest
```

---

## 🐳 Containerizare Docker

Aplicația este containerizată folosind `Dockerfile`, bazat pe imaginea `python:3.12-slim`.

### Build manual:

```bash
docker build -t veverita_app .
```

### Rulează aplicația:

```bash
docker run -d -p 5000:5000 --name veverita_container veverita_app
```

---

## 🔁 Automatizare CI/CD cu Jenkins

Proiectul include un `Jenkinsfile` cu etape declarative:

- **Checkout** – extragerea codului din `main_veverita`
- **Install** – instalarea dependențelor
- **Test** – rulare automată a testelor
- **Build Docker Image** – opțional, construire imagine Docker

Pipeline-ul se declanșează automat la fiecare `push`.

---

## ✅ Concluzie

Proiectul **Veverița App** ilustrează un ciclu complet DevOps pentru o aplicație Python:

- Cod curat, modular
- Testare automată cu `pytest`
- Containerizare cu Docker
- Automatizare CI/CD cu Jenkins

Toate acestea sunt documentate clar pentru rulare și prezentare fără Makefile.
