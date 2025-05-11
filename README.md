# Tutorial – Veverița App

### 1. Asigură-te că Make este instalat pe sistemul de operare linux
```bash
sudo apt install make
```

---

### 2. Rulează următoarele comenzi în terminalul tău Linux:

```bash
git clone --branch main_veverita https://github.com/USERNAME/curs_SCC_25_veverita.git
cd curs_SCC_25_veverita
make all
```

> Înlocuiește `USERNAME` cu numele tău de utilizator de GitHub dacă e cazul.

---

### 3. Deschide aplicația în browser:

- http://localhost:5000/veverita  
  sau  
- http://127.0.0.1:5000/veverita

---

# Despre proiect

Aplicația **Veverița App** din cadrul proiectului **SCC 2025** (student Curiman Teodor, grupa 441D) demonstrează un flux complet de dezvoltare și livrare continuă pentru o aplicație web simplă. Principalele componente sunt:

---

## 📚 Biblioteca de funcții pentru Veveriță

În `app/lib/biblioteca_animale.py` sunt definite două funcții:

- `culoare_veverita()` – returnează o descriere a culorii blănii veveriței.
- `descriere_veverita()` – oferă o descriere generală a veveriței.

---

## 🌐 Server Flask

În `app/main.py` este configurat un server Flask cu următoarele rute:

- `/veverita` – pagină principală cu linkuri către subpagini.
- `/culoare_veverita` – afișează rezultatul funcției `culoare_veverita()`.
- `/descriere_veverita` – afișează rezultatul funcției `descriere_veverita()`.

Se folosește `render_template_string` pentru a crea rapid un meniu HTML cu hyperlink-uri.

---

## ✅ Testare automată cu `pytest`

În `tests/test_biblioteca_animale.py` sunt definite teste care:

- verifică dacă `culoare_veverita()` returnează un șir ce conține o culoare (ex. „gri”, „roșcat”, „negru” etc.).
- validează că `descriere_veverita()` returnează un text de minimum 10 caractere.

Rulează testele local cu:
```bash
PYTHONPATH=$(pwd) pytest
```

---

## 🐳 Containerizare cu Docker

Fișierul `Dockerfile` definește o imagine Docker pe bază de `python:3.12-slim`, copiază codul sursă, instalează pachetele din `requirements.txt` și lansează serverul Flask.

Comenzi utile:

```bash
docker build -t veverita_app .
docker run -p 5000:5000 veverita_app
```

---

## 🔁 Automatizare CI/CD cu Jenkins

Un fișier `Jenkinsfile` este inclus pentru rularea automată a pașilor:

- **Checkout** – extrage codul din branch-ul `main_veverita`.
- **Install** – rulează `pip install -r requirements.txt`.
- **Test** – lansează `pytest` pentru testare automată.
- **Build Docker Image** – opțional, construiește imaginea Docker (`docker build`).

Pipeline-ul Jenkins rulează la fiecare `push` pentru a valida codul și a pregăti imaginea Docker.

---

## ⚙️ Makefile

Un fișier `Makefile` în rădăcina proiectului definește ținte pentru:

- `make build` – construiește imaginea Docker.
- `make run` – pornește containerul (după ce îl oprește pe cel vechi).
- `make stop` – oprește și șterge containerul.
- `make all` – execută `build` și `run` dintr-o singură comandă.

Pornirea completă a aplicației se face cu:

```bash
make all
```

---

## ✅ Concluzie

Acest proiect arată întregul ciclu de viață DevOps pentru o aplicație Python simplă: de la scrierea codului și testare, până la containerizare și CI/CD automatizat. README-ul și Makefile-ul permit rularea ușoară și prezentarea rapidă a aplicației.
