
Leopard 

📑 **Cuprins**

* [Descriere](#descriere)
* [Instalare și lansare](#instalare-și-lansare)
* [Containerizare Docker](#containerizare-docker)

---

## 🐆 Leopard

**Leopard** este o aplicație web simplă, construită cu \[Flask] în Python, ca parte a proiectului `curs_vcgj_25_441_animale`.

Scopul ei este să ofere o interfață web minimalistă, cu informații despre leopard, ușor de rulat atât local, cât și containerizat cu Docker.

---

## 🗂 Structură simplă

```
.
├── app/                      # Codul aplicației
│   └── lib/                  # Funcții despre animale
│   └── 441D_animal.py        # Aplicația principală Flask
├── Dockerfile                # Instrucțiuni pentru rulare în container
├── Makefile                  # Comenzi automate
├── quickrequirements.txt     # Dependențe minime
├── run                       # Script de pornire rapidă
├── dockerstart.sh            # Script pentru pornire în Docker
├── activeaza_venv            # Script de activare a mediului virtual
├── .gitignore                # Fișiere de ignorat în Git
├── LICENSE                   # Licență open-source
└── README.md                 # Acest fișier
```

---

## ⚙️ Instalare și lansare

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r quickrequirements.txt
python3 app/441D_animal.py
```

Accesează aplicația la adresa:
👉 [http://localhost:5011](http://localhost:5011)

---

## 🐳 Containerizare Docker

```bash
docker build -t leopard:v1 .
docker run -d -p 5011:5011 --name app leopard:v1
```

🛑 Oprire și ștergere container:

```bash
docker stop app
docker rm app
```

---

💡 **Docker** folosește imaginea `python`, instalează automat pachetele necesare din `quickrequirements.txt`, apoi rulează aplicația Flask în container. Astfel, aplicația e complet izolată și ușor de distribuit.

