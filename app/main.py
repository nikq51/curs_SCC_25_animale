from flask import Flask, render_template_string
from app.lib.biblioteca_animale import culoare_zebra, descriere_zebra  # funcțiile pentru zebra

app = Flask(__name__)

@app.route('/zebra')
def pagina_zebra():
    html = """
    <h1>Bine ați venit la pagina Zebra!</h1>
    <ul>
      <li><a href="/culoare_zebra">Vezi culoarea Zebra</a></li>
      <li><a href="/descriere_zebra">Vezi descrierea Zebra</a></li>
    </ul>
    """
    return render_template_string(html)

@app.route('/culoare_zebra')
def ruta_culoare():
    return f"<p>{culoare_zebra()}</p><p><a href='/zebra'>&larr; Înapoi</a></p>"

@app.route('/descriere_zebra')
def ruta_descriere():
    return f"<p>{descriere_zebra()}</p><p><a href='/zebra'>&larr; Înapoi</a></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
