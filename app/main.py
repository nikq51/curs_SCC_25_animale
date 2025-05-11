
from flask import Flask, render_template_string
from app.lib.biblioteca_animale import culoare_veverita, descriere_veverita

app = Flask(__name__)

@app.route('/veverita')
def pagina_veverita():
    html = """
    <h1>Bine ați venit la pagina veverita!</h1>
    <ul>
      <li><a href="/culoare_veverita">Vezi culoarea veverita</a></li>
      <li><a href="/descriere_veverita">Vezi descrierea veverita</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/culoare_veverita')
def ruta_culoare():
    return f"<p>{culoare_veverita()}</p><p><a href='/veverita'>&larr; Înapoi</a></p>"

@app.route('/descriere_veverita')
def ruta_descriere():
    return f"<p>{descriere_veverita()}</p><p><a href='/veverita'>&larr; Înapoi</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
