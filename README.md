# Proiect SCC – Aplicație Web pentru Animalul Koala

## Descriere
Proiectul constă în dezvoltarea unei aplicații web simple folosind Flask, containerizată cu Docker și automatizată cu Jenkins. Tema aleasă este animalul Koala.

Aplicația oferă următoarele rute:
- /koala – pagină principală cu opțiuni
- /koala/culoare – afișează culoarea animalului
- /koala/descriere – oferă o scurtă descriere

## Structura Proiectului

- koala.py – aplicația Flask  
- Dockerfile – configurația pentru imaginea Docker  
- Jenkinsfile – rularea automată CI/CD  
- requirements.txt – pachete necesare  
- app/lib/helper.py – funcție cu logica aplicată  
- app/tests/test_koala.py – testare automată  

## Comenzi utile

### Rulare locală:
python3 -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
python3 koala.py

### Rulare cu Docker:
docker build -t koala-app .  
docker run -p 5050:5050 koala-app

### Rulare testare automată:
pytest app/tests

### Pornire Jenkins:
java -jar jenkins.war

## Integrare Jenkins

Jenkins automatizează pașii:
- Crearea mediu virtual
- Instalare pachete
- Rulare pylint
- Testare cu pytest
- Construire și rulare Docker

## Teste

Fișierul test_koala.py verifică funcția culoare_koala din helper.py

Exemplu:
def test_culoare_koala():
    assert culoare_koala() == "cenușiu"
##curs_SCC_25_animale
