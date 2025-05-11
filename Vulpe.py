from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/vulpe">Vulpe</a></p>
    '''

@app.route("/vulpe")
def vulpe():
    return '''
        <h1>Vulpe</h1>
        <p><a href="/vulpe/descriere">Descriere</a></p>
        <p><a href="/vulpe/habitat">Habitat</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/vulpe/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Vulpii</h1>
        <p>{text}</p>
        <p><a href="/vulpe">Înapoi la Vulpe</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/vulpe/habitat")
def habitat():
    text = get_habitat()
    return f'''
        <h1>Habitatul Vulpii</h1>
        <p>{text}</p>
        <p><a href="/vulpe">Înapoi la Vulpe</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)
