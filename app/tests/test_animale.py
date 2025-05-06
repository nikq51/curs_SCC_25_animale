from app.lib.alimentatie import get_alimentatie
from app.lib.culoare import get_culoare

def check_alimentatie():
    alimentatie = get_alimentatie()
    if alimentatie == "Panda se hrănește în principal cu bambus.":
        return 1  # Corect
    else:
        return 0  # Gresit

def check_culoare():
    culoare = get_culoare()
    if culoare == "Panda are blana albă cu pete negre pe urechi, ochi și picioare.":
        return 1  # Corect
    else:
        return 0  # Gresit

# Apelează funcțiile și afisează rezultatele
if __name__ == "__main__":
    print("Test Alimentatie:", check_alimentatie())
    print("Test Culoare:", check_culoare())
