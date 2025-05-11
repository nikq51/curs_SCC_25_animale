# curs_vcgj_25_441_animale
# Aplicație Web Flask – Arici

Aceasta este o aplicație web construită cu Flask, în care sunt prezentate informații despre arici:
- Pagini descriptive: Despre, Curiozități, Zgomot, Emoji, Detalii, Prădători
- Navigare ușoară prin meniul principal

## Structură
- `animale.py`: punctul de pornire al aplicației
- `lib/`: conține funcțiile logice pentru fiecare pagină
- `tests/`: conține testele unitare pentru funcții

## Testare
- Teste scrise cu `pytest`
- Calitatea codului verificată cu `pylint`
- Executate automat în Jenkins

## Rulare locală
```bash
source app/activeaza_venv
python3 animale.py

