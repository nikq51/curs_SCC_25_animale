# curs_SCC_25_animale → puma.py

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Descriere versiune](#descriere-versiune)
3. [Configurare](#configurare)
4. [Exemple pagini web](#exemple-pagini-web)
5. [Testare cu pytest](#testare-cu-pytest)
6. [Verificare statică cu pylint](#verificare-statică-cu-pylint)
7. [Bibliografie](#bibliografie)

---

## Descriere aplicație

Aplicația puma.py este o aplicație web simplă, scrisă în Python cu framework-ul Flask. Aceasta oferă o experiență interactivă în lumea pumei — un animal sălbatic elegant și agil.

Utilizatorul poate naviga prin mai multe rute web care oferă:
- descrierea pumei,
- culoarea blănii,
- locurile în care trăiește.

Aplicația este structurată modular:
- logica auxiliară este în app/lib/helper.py,
- testele unitare sunt în app/tests/.

Poate fi rulată în Docker și integrată într-un pipeline Jenkins.

---

## Descriere versiune
### v1.0 – prima versiune

* Ruta principală / – [http://127.0.0.1:5001](http://127.0.0.1:5001)
* Rute adiționale:
  * /puma – pagina principală cu imagine și butoane
  * /puma/descriere – descriere generală
  * /puma/culoare – detalii despre blană
  * /puma/descriere/locatii – regiuni geografice unde trăiește

---

## Configurare

Aplicația rulează într-un mediu virtual Python:

bash
python3 -m venv .venv             # creează mediu virtual
source .venv/bin/activate         # activează venv (Linux/macOS)
.venv\Scripts\activate.bat      # pentru Windows (cmd)

pip install -r quickrequirements.txt   # instalează dependențele
python puma.py                         # pornește serverul Flask


Serverul pornește la: http://127.0.0.1:5001

---

## Exemple pagini web

### Pagina principală /

Afișează mesaj de întâmpinare și un buton către lumea pumei.

### Pagina /puma

Prezintă imaginea pumei și două butoane:
- Descriere
- Culoare

### Pagina /puma/descriere

Text cu informații generale despre puma și un buton pentru locurile unde trăiește.

### Pagina /puma/culoare

Detalii despre culoarea blănii pumei și link de întoarcere.

### Pagina /puma/descriere/locatii

Listă cu regiuni geografice: Munții Anzi, Stâncoși, America Centrală etc.

---

## Testare cu pytest

Testele sunt plasate în app/tests/ și includ:
- Teste pentru funcțiile din app/lib/helper.py
- Teste pentru rutele definite în puma.py

bash
pytest app/tests


---

## Verificare statică cu pylint

Pachetul pylint verifică stilul și posibile probleme în codul Python.

bash
pylint puma.py app/lib/*.py app/tests/*.py


Notă: problemele găsite nu opresc execuția pipeline-ului.

---

## Bibliografie

* https://github.com/crchende/sysinfo
* https://www.jenkins.io/
* https://docs.docker.com/
* https://flask.palletsprojects.com/
