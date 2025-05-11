# Proiect SCC – Aplicație Web pentru Animalul Lemur

## Descriere
Proiectul constă în realizarea unei aplicații web simple folosind Flask, containerizată cu Docker și automatizată cu Jenkins. Tema aleasă este reprezentarea animalului Lemur.

Aplicația oferă următoarele rute:
- /lemur – afișează pagina principală cu opțiuni
- /lemur/culoare – returnează culoarea animalului
- /lemur/descriere – returnează o descriere scurtă

## Structura Proiectului

- lemur.py – fișierul principal Flask 
- Dockerfile – imaginea Docker pentru rulare 
- Jenkinsfile – fișier pentru rularea CI în Jenkins 
- requirements.txt – dependințele Python 
- app/lib/helper.py – funcții helper pentru animal 
- app/tests/test_lemur.py – teste automate 

## Comenzi utile

### Rulare locală:
python3 -m venv .venv 
source .venv/bin/activate 
pip install -r requirements.txt 
python3 lemur.py

### Rulare cu Docker:
docker build -t lemur-app . 
docker run -p 5050:5050 lemur-app

### Accesare aplicație:
http://localhost:5050/lemur

## Integrare Jenkins

Prin Jenkins, aplicația este automatizată astfel:
- Instalare dependințe
- Rulare linting (pylint)
- Testare cu pytest
- Build și run Docker container

## Testare automată

Testele se află în app/tests/test_lemur.py și verifică:
- Răspunsul corect de la rute
- Funcțiile helper din app/lib/helper.py

Exemplu:
def test_culoare_lemur():
    assert culoare_lemur() == "gri cu coadă dungată"
