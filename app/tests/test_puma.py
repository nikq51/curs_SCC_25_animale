from puma import app

def test_pagina_principala():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bine ai venit" in response.data

def test_pagina_puma():
    client = app.test_client()
    response = client.get('/puma')
    assert response.status_code == 200
    assert b"Descriere Puma" in response.data or b"Informa" in response.data

def test_descriere_puma():
    client = app.test_client()
    response = client.get('/puma/descriere')
    assert response.status_code == 200
    assert b"mamifer" in response.data or b"solitar" in response.data

def test_culoare_puma():
    client = app.test_client()
    response = client.get('/puma/culoare')
    assert response.status_code == 200
    assert b"cafenie" in response.data or b"aurie" in response.data

def test_locatii_puma():
    client = app.test_client()
    response = client.get('/puma/descriere/locatii')
    assert response.status_code == 200
    assert b"Mun" in response.data or b"America" in response.data
