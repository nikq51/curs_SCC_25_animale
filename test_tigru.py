import unittest
from app.lib.helper import descriere_tigru, habitat_tigru, alimentatie_tigru

class TestTigru(unittest.TestCase):
    def test_descriere(self):
        self.assertIsInstance(descriere_tigru(), str)
    
    def test_habitat(self):
        self.assertIsInstance(habitat_tigru(), str)

    def test_alimentatie(self):
        self.assertIsInstance(alimentatie_tigru(), str)

if __name__ ==
