import pytest
from app.lib.biblioteca_animale import culoare_lup, descriere_lup

def test_culoare_lup():
    descriere = culoare_lup().lower()
    assert isinstance(descriere, str)
    # Verifică dacă blana este descrisă prin termeni tipici pentru lupi
    assert 'gri' in descriere or 'maro' in descriere or 'roșcat' in descriere or 'negru' in descriere

def test_descriere_lup():
    text = descriere_lup()
    assert isinstance(text, str)
    assert len(text) > 10
    assert 'lup' in text.lower() or 'mamifer' in text.lower()

