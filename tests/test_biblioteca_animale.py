import pytest
from app.lib.biblioteca_animale import culoare_alpaca, descriere_alpaca

def test_culoare_alpaca():
    assert isinstance(culoare_alpaca(), str)
    assert "alb" in culoare_alpaca().lower()

def test_descriere_alpaca():
    assert isinstance(descriere_alpaca(), str)
    assert len(descriere_alpaca()) > 10
