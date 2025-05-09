from app.lib import helper

def test_descriere_puma():
    assert isinstance(helper.descriere_puma(), str)
    assert "agil" in helper.descriere_puma().lower()

def test_culoare_puma():
    assert "cafenie" in helper.culoare_puma().lower() or "aurie" in helper.culoare_puma().lower()

def test_locatii_puma():
    locatii = helper.locatii_puma()
    assert isinstance(locatii, list)
    assert "Munții Anzi" in locatii
