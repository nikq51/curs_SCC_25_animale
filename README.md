# curs_vcgj_25_441_animale
# Aplicație Flask – ANIMALE (Leul)

Aceasta este o aplicație web simplă, care este  scrisă în Python folosind Flask, care prezintă informații despre leu: culoare și habitat. Proiectul este containerizat cu Docker și include un pipeline Jenkins pentru build, testare și rulare automată.

---

## Structura Proiectului

```
curs_SCC_25_animale/
├── animale.py                  # Punctul de intrare al aplicației Flask
├── app/
│   ├── lib/
│   │   ├── culoare.py          # Funcție ce returnează culoarea leului
│   │   └── habitat.py          # Funcție ce returnează habitatul leului
│   └── tests/
│       └── test_caracteristici.py  # Teste pentru culoare și habitat
├── Dockerfile                  # Dockerfile pentru containerizare
├── Jenkinsfile                 # Pipeline Jenkins pentru CI/CD
├── LICENSE                     
└── README.md                   # Documentația proiectului
```

---

## Rulare Locală cu Docker

### 1. Clonare repository

```bash
git clone https://github.com/nikq51/curs_SCC_25_animale.git
cd curs_SCC_25_animale
```

### 2. Build imagine Docker

```bash
docker build -t aplicatie-leu .
```

### 3. Rulează containerul

```bash
docker run -d -p 7070:7070 --name leut_container aplicatie-leu
```

### 4. Accesează aplicația

Deschide în browser: [http://localhost:7070](http://localhost:7070)

---

## Rute Disponibile

- `/` – Pagina principală
- `/leu` – Informație generală despre leu
- `/leu/culoare` – Culoarea tipică a leului
- `/leu/habitat` – Habitatul natural al leului

---

## Testare

Rulează testele local cu:

```bash
python3 -m app.tests.test_caracteristici
```

Testele verifică valorile returnate de funcțiile `get_culoare()` și `get_habitat()`.

---

## Jenkins Pipeline

Fișierul `Jenkinsfile` definește un pipeline automat cu următoarele etape:

- Listare directoare
- Build Docker
- Rulare teste
- Curățare container anterior
- Rulare container nou

---

## Autori

-- Andrei Calota
