from flask import Flask, render_template_string
from app.lib.biblioteca_animale import culoare_alpaca, descriere_alpaca

app = Flask(__name__)

@app.route('/alpaca')
def pagina_alpaca():
    html = """
    <h1>Bine ați venit la pagina Alpaca!</h1>
    <ul>
      <li><a href="/culoare_alpaca">Vezi culoarea Alpaca</a></li>
      <li><a href="/descriere_alpaca">Vezi descrierea Alpaca</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/culoare_alpaca')
def ruta_culoare():
    return f"<p>{culoare_alpaca()}</p><p><a href='/alpaca'>&larr; Înapoi</a></p>"

@app.route('/descriere_alpaca')
def ruta_descriere():
    return f"<p>{descriere_alpaca()}</p><p><a href='/alpaca'>&larr; Înapoi</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

