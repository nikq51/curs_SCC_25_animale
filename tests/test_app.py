import logging
import pytest

from app.lib.biblioteca_Animale import get_habitat_manul, get_dieta_manul

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def test_habitat_manul():
    logger.info("Testare get_habitat_manul...")
    habitat = get_habitat_manul()
    assert isinstance(habitat, str), "Habitatul nu este string"
    assert len(habitat) > 0, "Habitatul este gol"
    assert "Manulul" in habitat, "Lipsă 'Manulul' din habitat"
    assert "Asia Centrală" in habitat, "Lipsă 'Asia Centrală' din habitat"

def test_dieta_manul():
    logger.info("Testare get_dieta_manul...")
    dieta = get_dieta_manul()
    assert isinstance(dieta, str), "Dieta nu este string"
    assert len(dieta) > 0, "Dieta este goală"
    assert "pika" in dieta, "Lipsă 'pika' din dietă"
    assert "rozătoare" in dieta, "Lipsă 'rozătoare' din dietă"
