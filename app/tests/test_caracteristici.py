from app.lib.info_general import get_homepage_info, get_urs_info
from app.lib.alimentatie import get_alimentatie
from app.lib.specii import get_specii

def test_get_homepage_info():
    expected = "Tema: Animale"
    rezultat = get_homepage_info()
    if rezultat == expected:
        print("test_get_homepage_info: CORECT")
    else:
        print("test_get_homepage_info: GREȘIT")

def test_get_urs_info():
    expected = "Animal: Urs"
    rezultat = get_urs_info()
    if rezultat == expected:
        print("test_get_urs_info: CORECT")
    else:
        print("test_get_urs_info: GREȘIT")

def test_get_alimentatie():
    expected = "Ursul este omnivor: consumă fructe, pești, carne și plante."
    rezultat = get_alimentatie()
    if rezultat == expected:
        print("test_get_alimentatie: CORECT")
    else:
        print("test_get_alimentatie: GREȘIT")

def test_get_specii():
    expected = "Există mai multe specii de urși: urs brun, urs polar, urs panda, etc."
    rezultat = get_specii()
    if rezultat == expected:
        print("test_get_specii: CORECT")
    else:
        print("test_get_specii: GREȘIT")

if __name__ == "__main__":
    test_get_homepage_info()
    test_get_urs_info()
    test_get_alimentatie()
    test_get_specii()
