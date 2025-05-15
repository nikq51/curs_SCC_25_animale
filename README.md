##curs_SCC_25_animale
# Zebra App – Proiect SCC 2025 🦓  
*Baranga Andreea, grupa 441D*

---

## 🔧 Tutorial de instalare și rulare

Asigură-te că ai instalat Docker pe sistemul tău.  
Pentru Ubuntu:
```bash
sudo apt update
sudo apt install docker.io
Apoi, rulează următoarele comenzi într-un terminal Linux:

bash
Copier
git clone --branch main_baranga_andreea https://github.com/nikq51/curs_SCC_25_animale.git
cd curs_SCC_25_animale
docker build -t zebra_app .
docker run -p 5000:5000 zebra_app
Deschide în browser:

http://localhost:5000/zebra
sau

http://127.0.0.1:5000/zebra

📝 Descrierea proiectului
Zebra App este o aplicație web simplă realizată în cadrul cursului Sisteme de Calcul și Comunicații (SCC). Proiectul are ca scop demonstrarea unui flux de dezvoltare complet pentru o aplicație web containerizată, care oferă informații despre un animal ales: zebra.

📚 Biblioteca de funcții pentru Zebra
În app/lib/biblioteca_animale.py au fost definite două funcții:

culoare_zebra() – returnează o descriere simplă a culorii caracteristice (alb-negru)

descriere_zebra() – oferă informații generale despre zebra

🌐 Server Flask
În app/main.py este implementat un server Flask cu următoarele rute:

/zebra – pagina principală dedicată zebrei, cu linkuri către subpagini

/culoare_zebra – afișează rezultatul returnat de funcția culoare_zebra()

/descriere_zebra – afișează rezultatul returnat de funcția descriere_zebra()

Pentru simplitate, am folosit render_template_string pentru a genera o interfață HTML minimalistă, direct din cod.

✅ Testare automată cu pytest
În tests/test_biblioteca_animale.py sunt definite teste care:

Verifică faptul că culoare_zebra() returnează un șir ce conține o culoare validă

Verifică faptul că descriere_zebra() returnează un șir cu minimum 10 caractere

Testele pot fi rulate local astfel:

bash
Copier
PYTHONPATH=$(pwd) pytest
🐳 Containerizare Docker
Aplicația este ambalată într-un container Docker.

🔹 Dockerfile
Fișierul Dockerfile:

Folosește imaginea python:3.12-slim

Copiază codul sursă în container

Instalează dependențele definite în requirements.txt

Pornește serverul Flask

🔹 Comenzi utile
Construirea imaginii:

bash
Copier
docker build -t zebra_app .
Rularea containerului:

bash
Copier
docker run -p 5000:5000 zebra_app
📂 Structura proiectului
css
Copier
├── app/
│   ├── lib/
│   │   └── biblioteca_animale.py
│   └── main.py
├── tests/
│   └── test_biblioteca_animale.py
├── requirements.txt
├── Dockerfile
├── README.md
📄 Exemple de output
Navigând la http://localhost:5000/zebra, utilizatorul va vedea:

Un meniu HTML simplu cu două linkuri:

/culoare_zebra → "Zebrele au un tipar distinctiv de dungi negre și albe."

/descriere_zebra → "Zebra este un animal erbivor care trăiește în savanele Africii. Este cunoscută pentru dungile sale unice."
