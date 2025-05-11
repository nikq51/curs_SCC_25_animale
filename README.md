
# 🐆 Pantera Neagră

📑 **Cuprins**
- [🐾 Prezentare generală](#-prezentare-generală)
- [⚙️ Cum se instalează și pornește aplicația](#️-cum-se-instalează-și-pornește-aplicația)
- [🐳 Rulare cu Docker](#-rulare-cu-docker)
- [🗂 Structură simplă](#-structură-simplă)

---

## 🐾 Prezentare generală

Aplicația **Pantera Neagră** este realizată în Python folosind [Flask]. Face parte din proiectul `curs_SCC_25_animale` și oferă o interfață web care afișează informații esențiale despre această felină fascinantă.

Este concepută pentru a fi:
- ușor de rulat local;
- portabilă și containerizabilă prin Docker.

---

## 🗂 Structură simplă

```text
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


## ⚙️ Cum se instalează și pornește aplicația

1. Creează și activează un mediu virtual:
```bash
python3 -m venv venv
source venv/bin/activate
````

2. Instalează dependințele:

```bash
pip install -r quickrequirements.txt
```

3. Rulează aplicația Flask:

```bash
python3 app/441D_animal.py
```

4. Deschide browserul și accesează:
   🌐 (http://172.17.0.2:5011/animal)

---

## 🐳 Rulare cu Docker

Poți rula aplicația direct într-un container Docker:

### ▶️ Build și lansare container:

```bash
docker build -t animal:v01 .
docker run --name animal -p 8020:5011 animal:v01
```

Aplicația va fi disponibilă la:
🌐 (http://172.17.0.2:5011/animal)

### 🧹 Oprire și ștergere container:

```bash
docker stop animal
docker rm animal
```

---
