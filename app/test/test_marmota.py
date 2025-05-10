import unittest
from app.lib.descriere_marmota import get_descriere
from app.lib.mancare_marmota import get_mancare_marmota

class TestCapibaraInfo(unittest.TestCase):
    def test_descriere(self):
        descriere = get_descriere()
        self.assertIsInstance(descriere, str)
        self.assertTrue("Marmotele" in descriere)

    def test_mancare(self):
        mancare = get_mancare_marmota()
        self.assertIsInstance(mancare, str)
        self.assertTrue("Frunze" in mancare)

if __name__ == '__main__':
    unittest.main()
