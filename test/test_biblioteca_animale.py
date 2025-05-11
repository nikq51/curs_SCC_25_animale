import pytest
from app.lib.biblioteca_animale import culoare_veverita, descriere_veverita

def test_culoare_veverita():
    descriere = culoare_veverita().lower()
    assert isinstance(descriere, str)
    # Verifică dacă cuvântul 'alb' apare în descrierea returnată
    assert 'alb' in descriere or 'gri' in descriere or 'roșcat' in descriere or 'brun' in descriere or 'negru' in descriere

def test_descriere_veverita():
    assert isinstance(descriere_veverita(), str)
    assert len(descriere_veverita()) > 10
