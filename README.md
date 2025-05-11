#SCC_proiect
# Aplicație Flask – Urs

Aceasta este o aplicație web scrisă în Python folosind Flask, care oferă informații despre animalul urs. Aplicația este containerizată cu Docker și folosește Jenkins pentru rulare automată.

## Funcționalitate

Aplicația oferă următoarele rute:

- `/` – Pagina principală cu titlul temei și butoane de navigare
- `/urs` – Informații generale despre urs
- `/urs/alimentatie` – Informații despre alimentația ursului
- `/urs/specii` – Informații despre specii de urși

## Structura proiectului

```
curs_SCC_25_animale/
├── animale.py                 # Aplicația principală Flask
├── Dockerfile                # Fișier pentru containerizare
├── Jenkinsfile               # Pipeline pentru Jenkins
└── app/
    ├── lib/
    │   ├── info_general.py   # Funcții pentru homepage și /urs
    │   ├── alimentatie.py    # Funcție pentru alimentație
    │   └── specii.py         # Funcție pentru specii
    └── tests/
        └── test_caracteristici.py   # Teste simple
```

## Rulare aplicație

### Cu Docker

#### Build imagine

```bash
docker build -t aplicatie-urs .
```

#### Rulare container

```bash
docker run -p 9090:9090 --name urs_container aplicatie-urs
```

Aplicația poate fi accesată la: http://localhost:9090

## Jenkins

Fișierul Jenkinsfile automatizează următoarele etape:

1. Construirea imaginii Docker
2. Rularea testelor definite
3. Curățarea oricărui container existent
4. Pornirea aplicației într-un container nou

## Testare

Testele validează funcțiile implementate în fișierele din `lib` și compară rezultatele cu textele așteptate:

```bash
python3 -m app.tests.test_caracteristici
```

Rezultatele sunt afișate în consolă ca: `CORECT` sau `GREȘIT`.

## Autor

Marina Dragan
