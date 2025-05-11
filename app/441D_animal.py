# app/441D_animal.py
from flask import Flask, render_template_string
# Import the actual names and alias them to the names used in the routes
from app.lib.biblioteca_animal import descriere_scurta_animal as descriere_scurta, chestii_specifice_pantera as informatii_interesante

# Rest of your Flask code remains the same,
# as it calls descriere_scurta() and opere_autor()
app = Flask(__name__)

@app.route('/animal')
def pagina_index_animal():
    html = """
    <h1>Pantera</h1>
    <ul>
      <li><a href="/descriere_scurta_pantera">Descriere scurta a Panterei negre</a></li>
      <li><a href="/chestii_specifice_pantera">Informatii interesante despre Pantera neagra</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/descriere_scurta_pantera')
def ruta_descriere_scurta():
    # Calls the imported function aliased as descriere_scurta
    return f"<p>{descriere_scurta()}</p><p><a href='/animal'>&larr; Înapoi</a></p>"

@app.route('/chestii_specifice_pantera')
def ruta_animal():
    # Calls the imported function aliased as opere_autor
    return f"<p>{informatii_interesante()}</p><p><a href='/animal'>&larr; Înapoi</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True) # Using port 5011 and debug
