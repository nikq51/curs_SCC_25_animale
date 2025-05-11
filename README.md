🐆 Pantera Neagră
📑 Cuprins

Prezentare generală

Cum se instalează și pornește aplicația

Rulare cu Docker

🐾 Prezentare generală
Aplicația Pantera Neagră este realizată în Python. Face parte din proiectul curs_SCC_25_animale și oferă o pagină web cu informații esențiale despre această felină.

Este gândită să fie ușor de pornit local, dar și pregătită pentru a fi rulată într-un container Docker, fără pași complicați.

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
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r quickrequirements.txt
Rulează aplicația:

bash
Copy
Edit
python3 app/441D_animal.py
Apoi accesează în browser:
🌐 (http://172.17.0.2:5011/animal)

🐳 Rulare cu Docker
Poți rula aplicația și într-un container, folosind comenzi simple:

▶️ Lansare container:
bash
Copy
Edit
docker run -- name animal -p 8020:5011 animal:v01
🧹 Oprire și ștergere:
bash
Copy
Edit
docker stop pantera_container
docker rm pantera_container
