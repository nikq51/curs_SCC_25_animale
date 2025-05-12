import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from app.cal import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_culori_cal(client):
    """Test pentru ruta /cal/culoare"""
    response = client.get('/cal/culoare')
    assert response.status_code == 200
    assert b"Culoarea unui cal poate varia" in response.data

def test_descriere_cal(client):
    """Test pentru ruta /cal/descriere"""
    response = client.get('/cal/descriere')
    assert response.status_code == 200
    assert b"Calul este un mamifer" in response.data

def test_cal(client):
    """Test pentru ruta /cal"""
    response = client.get('/cal')
    assert response.status_code == 200
    assert b"Aceasta este pagina dedicata calului" in response.data
