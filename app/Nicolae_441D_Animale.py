from flask import Flask, url_for
from lib.biblioteca_Animale import get_habitat_manul, get_dieta_manul

app = Flask(__name__)

@app.route("/")
def index():
    """Pagina principală a aplicației."""
    # Inițial, link doar către pagina Manulului
    html = "<h1>Proiect VCGJ - Animale</h1>"
    html += "<p>Bine ați venit! Acest proiect prezintă informații despre diverse animale.</p>"
    html += f"<a href='{url_for('info_manul')}'>Informații despre Manul</a><br>"
    # Pe viitor, aici se vor adăuga link-uri către alte animale adăugate de colegi
    return html

@app.route("/manul")
def info_manul():
    """Pagina cu informații generale despre Manul și link-uri către detalii."""
    habitat = get_habitat_manul()
    dieta = get_dieta_manul()

    html = "<h2>Informații despre Manul (Pisica Pallas)</h2>"
    html += f"<p><a href='{url_for('habitat_manul')}'>Vezi habitatul Manulului</a></p>"
    html += f"<p><a href='{url_for('dieta_manul')}'>Vezi dieta Manulului</a></p>"
    html += "<hr>"
    html += "<h3>Detalii rapide:</h3>"
    html += f"<p><strong>Habitat pe scurt:</strong> {habitat.split('.')[0]}.</p>" # Afișăm doar prima propoziție ca preview
    html += f"<p><strong>Dietă pe scurt:</strong> {dieta.split('.')[0]}.</p>"   # Afișăm doar prima propoziție ca preview
    html += f"<br><a href='{url_for('index')}'>Înapoi la pagina principală</a>"
    return html

@app.route("/manul/habitat")
def habitat_manul():
    """Pagină dedicată habitatului Manulului."""
    info = get_habitat_manul()
    html = f"<h2>Habitatul Manulului</h2>"
    html += f"<p>{info}</p>"
    html += f"<br><a href='{url_for('info_manul')}'>Înapoi la pagina Manulului</a>"
    html += f"<br><a href='{url_for('index')}'>Înapoi la pagina principală</a>"
    return html

@app.route("/manul/dieta")
def dieta_manul():
    """Pagină dedicată dietei Manulului."""
    info = get_dieta_manul()
    html = f"<h2>Dieta Manulului</h2>"
    html += f"<p>{info}</p>"
    html += f"<br><a href='{url_for('info_manul')}'>Înapoi la pagina Manulului</a>"
    html += f"<br><a href='{url_for('index')}'>Înapoi la pagina principală</a>"
    return html

if __name__ == "__main__":
    # Rulează serverul de dezvoltare Flask
    # Accesibil la http://127.0.0.1:5000/ (sau portul specificat)
    # Modul debug este util în dezvoltare pentru a vedea erorile și a reîncărca automat la modificări
    app.run(debug=True, host='0.0.0.0', port=5001) # Am schimbat portul pentru a nu se suprapune cu exemplul din documentație
