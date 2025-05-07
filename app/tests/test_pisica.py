from pisica import app

def test_pagina_principala():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bine ai venit la lumea pisicilor" in response.data

def test_pagina_pisica():
    client = app.test_client()
    response = client.get('/pisica')
    assert response.status_code == 200
    assert b"Descriere pisica" in response.data

def test_descriere_pisica():
    client = app.test_client()
    response = client.get('/pisica/descriere')
    assert response.status_code == 200
    assert b"animal bland" in response.data

def test_culoare_pisica():
    client = app.test_client()
    response = client.get('/pisica/culoare')
    assert response.status_code == 200
    assert b"gri cu alb" in response.data

def test_nume_pisica():
    client = app.test_client()
    response = client.get('/pisica/descriere/nume')
    assert response.status_code == 200
    assert b"Mitzi" in response.data