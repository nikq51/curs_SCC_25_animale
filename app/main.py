from flask import Flask, render_template_string
from app.lib.biblioteca_animale import culoare_lup, descriere_lup

app = Flask(__name__)

@app.route('/lup')
def pagina_lup():
    html = """
    <h1>Bine ați venit la pagina lup!</h1>
    <ul>
      <li><a href="/culoare_lup">Vezi culoarea lup</a></li>
      <li><a href="/descriere_lup">Vezi descrierea lup</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/culoare_lup')
def ruta_culoare():
    return f"<p>{culoare_lup()}</p><p><a href='/lup'>&larr; Înapoi</a></p>"

@app.route('/descriere_lup')
def ruta_descriere():
    return f"<p>{descriere_lup()}</p><p><a href='/lup'>&larr; Înapoi</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
