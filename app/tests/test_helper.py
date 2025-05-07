from app.lib import helper

def test_descriere_pisica_logica():
    text = helper.descriere_pisica()
    assert isinstance(text, str)
    assert "bland" in text

def test_culoare_pisica_logica():
    text = helper.culoare_pisica()
    assert "gri" in text.lower()

def test_lista_nume_pisici():
    lista = helper.lista_nume_pisici()
    assert isinstance(lista, list)
    assert "Mitzi" in lista