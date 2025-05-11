import unittest
from app.lib.helper import descriere_tigru, culoare_tigru, lista_nume_tigri

class TestHelperTigru(unittest.TestCase):

    def test_descriere_tigru(self):
        descriere = descriere_tigru()
        self.assertIn("Tigrul", descriere)
        self.assertIsInstance(descriere, str)

    def test_culoare_tigru(self):
        culoare = culoare_tigru()
        self.assertIn("portocalie", culoare)
        self.assertIn("negre", culoare)

    def test_lista_nume_tigri(self):
        nume = lista_nume_tigri()
        self.assertIsInstance(nume, list)
        self.assertGreaterEqual(len(nume), 3)
        self.assertIn("Shere Khan", nume)

if __name__ == '__main__':
    unittest.main()

