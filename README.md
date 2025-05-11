# 🐭 Raton

Raton este o aplicație web simplă, construită cu [Flask] în Python. Scopul ei este să demonstreze cum poți construi rapid o aplicație web ușor de testat, containerizat și integrat într-un flux CI/CD cu Jenkins.

## 🚀 Ce face

- Servește o interfață web de bază
- E pregătită pentru testare automată
- Se rulează în containere Docker
- Integrare ușoară cu Jenkins pentru CI

## 🗂 Structură simplă

- `raton.py` – fișierul principal al aplicației
- `Dockerfile` – pentru rulare în container
- `tests/` – loc pentru testele automate

## Instalare si lansare

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
python3 raton.py
```

## Testare


Testele sunt scrise în `app/test/testare.py` și pot fi rulate cu:

```bash
python3 -m unittest app.test.testare
```

