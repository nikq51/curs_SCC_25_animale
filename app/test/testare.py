import unittest
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

class TestVidraInfo(unittest.TestCase):
    def test_descriere(self):
        descriere = get_descriere()
        self.assertIsInstance(descriere, str)
        self.assertTrue("Vidra" in descriere)

    def test_habitat(self):
        habitat = get_habitat()
        self.assertIsInstance(habitat, str)
        self.assertTrue("habitat" in habitat.lower() or "apă" in habitat.lower())

if __name__ == '__main__':
    unittest.main()
