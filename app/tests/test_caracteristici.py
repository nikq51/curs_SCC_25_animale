from app.lib.culoare import get_culoare
from app.lib.habitat import get_habitat

def test_get_culoare():
    expected = "Leul are o culoare aurie, galben deschis sau maro deschis, ajutându-l să se camufleze în savană."
    print("test_get_culoare:", "CORECT" if get_culoare() == expected else "GREȘIT")

def test_get_habitat():
    expected = "Leul trăiește în habitate deschise: savane, păduri rare și câmpii din Africa sub-sahariană și India."
    print("test_get_habitat:", "CORECT" if get_habitat() == expected else "GREȘIT")

if __name__ == "__main__":
    test_get_culoare()
    test_get_habitat()
