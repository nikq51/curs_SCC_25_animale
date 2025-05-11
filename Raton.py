from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

app = Flask(__name__)


@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/raton">Raton</a></p>
    '''

@app.route("/raton")
def raton():
    return '''
        <h1>Raton</h1>
        <p><a href="/raton/descriere">Descriere</a></p>
        <p><a href="/raton/habitat">Habitat</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/raton/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Ratonului</h1>
        <p>{text}</p>
        <p><a href="/raton">Înapoi la Raton</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/raton/habitat")
def habitat():
    text = get_habitat()
    return f'''
        <h1>Habitatul Ratonului</h1>
        <p>{text}</p>
        <p><a href="/raton">Înapoi la Raton</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)
