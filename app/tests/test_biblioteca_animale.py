"""Teste pentru biblioteca_animale."""

from lib import biblioteca_animale as b_animale

def test_simplu():
    """Test simplu de validare."""
    assert b_animale.salut() == "Salut din biblioteca_animale!"

def test_culoare_arici():
    """Testeaza culoarea ariciului."""
    cul = b_animale.culoare_arici()
    if cul == "gri":
        assert True
    else:
        assert False

def test_hrana_arici():
    """Testeaza hrana ariciului."""
    inf = b_animale.hrana_arici()
    if inf == "insecte":
        assert True
    else:
        assert False

def test_invelisul_corpului_arici():
    """Testeaza invelisul ariciului."""
    inf = b_animale.invelisul_corpului_arici()
    if inf == "tepi":
        assert True
    else:
        assert False

