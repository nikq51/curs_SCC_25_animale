# Proiect: Bizon 🦬

Aplicație web dezvoltată în Python folosind Flask, care oferă informații despre bizon (descriere și habitat). Include testare unitară, analiză statică a codului și pipeline de livrare continuă cu Jenkins și Docker.

---

## 📁 Structura proiectului

- `Bizon.py` – Aplicația principală Flask care definește rutele web.
- `testare.py` – Teste unitare pentru funcțiile `get_descriere()` și `get_habitat()`.
- `Dockerfile.txt` – Fișier de configurare pentru containerizarea aplicației.
- `Jenkinsfile.txt` – Definirea pipeline-ului CI/CD.
- `app/lib/descriere.py` – Funcție care oferă descrierea bizonului.
- `app/lib/habitat.py` – Funcție care returnează informații despre habitatul bizonului.
- `quickrequirements.txt` sau `requirements.txt` – Lista pachetelor necesare.

---

## 🚀 Rulare locală

### 1. Instalare dependințe

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
