## Proiect Delfini – Aplicație Web cu Flask

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Configurare](#configurare)
3. [Exemple pagini web](#exemple-pagini-web)
4. [Testare cu unittest](#testare-cu-unittest)
5. [Verificare statică cu pylint](#verificare-statică-cu-pylint)

---

## Descriere aplicație

Aplicația `delfin.py` este o aplicație web scrisă în Python cu framework-ul Flask. Aceasta oferă o interfață interactivă despre delfini – mamifere marine inteligente și sociale.

Rutele aplicației oferă:
- descrierea delfinilor,
- sunetele produse,
- habitatul acestora,
- regiunile geografice unde sunt întâlniți.

Structura aplicației:
- fișiere logice în `app/lib/` (`sunete.py`, `habitat.py`, `aparitie.py`)
- testele în `app/test/test_delfin.py`
- fișiere statice în `static/images/`
- aplicația web principală în `delfin.py`

Aplicația se rulează într-un container Docker și poate fi gestionată dintr-un pipeline Jenkins.

- Ruta principală: [http://localhost:5000](http://localhost:5000)
- Rute adiționale:
  - `/delfin` – imagine + butoane
  - `/delfin/sunete` – descriere + imagine `com.jpg`
  - `/delfin/habitat` – descriere + imagine `hab.jpg`
  - `/delfin/aparitie` – descriere + imagine `delf1.jpg`

## Configurare

Aplicația rulează direct în Docker:

1. Construirea imaginii

docker build -t aplicatie-delfin 
2. Rularea containerului

docker run -d -p 5000:5000 --name delfin_container aplicatie-delfin
Apoi deschide în browser:

http://localhost:5000

Exemple pagini web
/
Pagina de start – titlu aplicație, autor, buton către secțiunea principală.

/delfin
Imagine + linkuri către celelalte secțiuni.

/delfin/sunete
Text despre comunicarea acustică + imagine com.jpg.

/delfin/habitat
Descrierea habitatului + imagine hab.jpg.

/delfin/aparitie
Zone geografice + imagine delf1.jpg.

Testare cu unittest
Testele din app/test/test_delfin.py verifică:

-dacă funcțiile returnează str

-dacă textul conține cuvintele-cheie corecte


python3 -m unittest app.test.test_delfin
