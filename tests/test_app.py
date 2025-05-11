import logging
import sys
import os

# Configurare basic logging (opțional, dar bun pentru debug)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Adăugare director rădăcină la sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from app.lib.biblioteca_Animale import get_habitat_manul, get_dieta_manul

def test_habitat_manul():
    logger.info("Testare get_habitat_manul...")
    habitat = get_habitat_manul()
    assert isinstance(habitat, str), "Habitatul nu este string"
    assert len(habitat) > 0, "Habitatul este gol"
    assert "Manulul" in habitat, "Lipsă 'Manulul' din habitat"
    assert "Asia Centrală" in habitat, "Lipsă 'Asia Centrală' din habitat"
    logger.info("get_habitat_manul: PASS")

def test_dieta_manul():
    logger.info("Testare get_dieta_manul...")
    dieta = get_dieta_manul()
    assert isinstance(dieta, str), "Dieta nu este string"
    assert len(dieta) > 0, "Dieta este goală"
    assert "pika" in dieta, "Lipsă 'pika' din dietă"
    assert "rozătoare" in dieta, "Lipsă 'rozătoare' din dietă"
    logger.info("get_dieta_manul: PASS")

if __name__ == "__main__":
    logger.info("--- START TESTE ---")
    test_habitat_manul()
    test_dieta_manul()
    logger.info("--- SFÂRȘIT TESTE: Toate testele apelate au trecut ---")
    # Scriptul va ieși cu cod 0 dacă ajunge aici.
    # Dacă un assert eșuează, scriptul se oprește și iese cu cod non-zero.
