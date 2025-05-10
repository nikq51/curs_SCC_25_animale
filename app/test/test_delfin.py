import unittest
from app.lib.habitat import get_habitat
from app.lib.aparitie import get_aparitie
from app.lib.sunete import get_sunete

class TestDelfinInfo(unittest.TestCase):

    def test_habitat(self):
        rezultat = get_habitat()
        self.assertIsInstance(rezultat, str)
        self.assertTrue("ocean" in rezultat.lower() or "mare" in rezultat.lower())

    def test_aparitie(self):
        rezultat = get_aparitie()
        self.assertIsInstance(rezultat, str)
        self.assertTrue("corp" in rezultat.lower() or "înotătoare" in rezultat.lower())

    def test_sunete(self):
        rezultat = get_sunete()
        self.assertIsInstance(rezultat, str)
        self.assertTrue("sunet" in rezultat.lower() or "ecolocație" in rezultat.lower())

if __name__ == "__main__":
    unittest.main()
