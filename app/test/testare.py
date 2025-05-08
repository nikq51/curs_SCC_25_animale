import unittest
from app.lib.descriere import get_descriere
from app.lib.culoare import get_culoare

class TestCapibaraInfo(unittest.TestCase):
    def test_descriere(self):
        descriere = get_descriere()
        self.assertIsInstance(descriere, str)
        self.assertTrue("Capibara" in descriere)

    def test_culoare(self):
        culoare = get_culoare()
        self.assertIsInstance(culoare, str)
        self.assertTrue("culoare" in culoare or "blana" in culoare)

if __name__ == '__main__':
    unittest.main()
