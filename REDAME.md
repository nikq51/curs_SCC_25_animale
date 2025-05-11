# Flask App - Biblioteca Animale

Proiectul este o aplicație web dezvoltată în Flask care gestionează și prezintă informații despre animale, mai exact despre cal. Aplicația include endpoint-uri pentru a descrie un cal și culorile disponibile.

## Funcționalități:
- `/cal`: Afișează o pagină dedicată calului.
- `/cal/culoare`: Afișează informații despre culorile posibile ale unui cal.
- `/cal/descriere`: Afișează o descriere generală despre cal.

---

## Structura proiectului:
├── app
│ ── 441D_animale.py # Scriptul Flask principal
│ ── biblioteca_animale.py # Logica aplicației și definițiile funcțiilor
│ 
│
│
├── Dockerfile # Dockerfile pentru containerizare
├── Jenkinsfile # Pipeline pentru Jenkins
├── requirements.txt # Dependențele proiectului
└── README.md # Documentația proiectului

---

## Instalare și Rulare

### 1. Clonare repository:
```bash
git clone https://github.com/nikq51/curs_SCC_25_animale.git
cd curs_SCC_25_animale

#Constrtuirea fisierului Docker
docker build -t flask_app_cal .

#Rularea containerului
docker run -d --name flask_app_cal_container -p 5000:5000 flask_app_cal
Testare API

#Pentru a verifica endpoint-urile, poți folosi curl sau deschide direct în browser:

curl http://localhost:5000/cal
curl http://localhost:5000/cal/culoare
curl http://localhost:5000/cal/descriere

#Sau în browser:

    http://localhost:5000/cal

    http://localhost:5000/cal/culoare

    http://localhost:5000/cal/descriere

#Integrare Jenkins

Proiectul este configurat să fie rulat printr-un pipeline de Jenkins. Jenkinsfile include pașii pentru:

    Clonarea repository-ului

    Construirea imaginii Docker

    Rularea containerului

    Testarea API-ului

#Autori

    Stefania Ionescu - Developer

    nikq51 - Repository owner

#Licență

Proiectul este licențiat sub licența MIT.
