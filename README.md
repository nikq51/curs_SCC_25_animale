# Tema: Animale - Panda

## Descriere

Acest proiect este o aplicație web simplă realizată în Flask, care oferă informații despre panda: culoare și alimentație.  
Proiectul este realizat de **Chirtoacă Andreea**, grupa 441D.

Aplicația conține:
- o interfață web cu rute dedicate pentru panda
- testare automată
- integrare Docker
- pipeline de CI cu Jenkins

---

## Cuprins

- [Structura proiectului](#structura-proiectului)
- [Descriere fișiere](#descriere-fișiere)
- [Utilizare](#utilizare)
- [Pipeline Jenkins](#pipeline-jenkins)
- [Git Workflow](#git-workflow)
- [Testare](#testare)

---

## Structura proiectului

```
.
├── animale.py
├── app
│   ├── lib
│   │   ├── alimentatie.py
│   │   ├── culoare.py
│   └── tests
│       └── test_animale.py
├── Dockerfile
├── Jenkinsfile
├── LICENSE
└── README.md
```

---

## Descriere fișiere

- `animale.py` – Aplicația principală Flask, definește rutele web.
- `app/lib/alimentatie.py` – Conține funcția care returnează descrierea alimentației panda.
- `app/lib/culoare.py` – Conține funcția care returnează informații despre culoarea panda.
- `app/tests/test_animale.py` – Teste pentru funcțiile `get_alimentatie` și `get_culoare`.
- `Dockerfile` – Definește imaginea Docker pentru rularea aplicației Flask.
- `Jenkinsfile` – Definește pipeline-ul Jenkins (testare, build, rulare container).
- `LICENSE` – Licența proiectului.
- `README.md` – Documentația proiectului (acest fișier).

---

## Utilizare

### Rulare locală

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
python animale.py
```

Accesează aplicația în browser la: [http://localhost:5000](http://localhost:5000)

---

### Rulare în Docker

```bash
docker build -t app-panda .
docker run -d -p 5000:5000 --name app app-panda
```

---

## Pipeline Jenkins

Definit în `Jenkinsfile`. Include:

1. Listare directoare
2. Rulare teste
3. Build Docker image
4. Curățare și rulare container

---

## Git Workflow

Proiectul folosește două branch-uri:

- `main_chirtoaca_andreea` – versiunea stabilă
- `devel_chirtoaca_andreea` – dezvoltare activă

Fluxul de lucru:

1. Se lucrează pe `devel_chirtoaca_andreea`
2. Se testează și se face `commit + push`
3. Se face `merge` în `main_chirtoaca_andreea` după verificare

---

## Testare

Testele sunt definite în `app/tests/test_animale.py`.  
Verifică funcțiile:

- `get_alimentatie()` – trebuie să returneze alimentația corectă a panda
- `get_culoare()` – trebuie să returneze descrierea culorii panda

Rulare:

```bash
python app/tests/test_animale.py
```


