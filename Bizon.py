from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat


app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/bizon">Bizonul</a></p>
    '''

@app.route("/bizon")
def bizon():
    return '''
        <h1>Bizon</h1>
        <p><a href="/bizon/descriere">Descriere</a></p>
        <p><a href="/bizon/habitat">Habitat</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/bizon/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Bizlonului</h1>
        <p>{text}</p>
        <p><a href="/bizon">Înapoi la Bizon</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/bizon/habitat")
def habitat():
    text = get_habitat()
    return f'''
        <h1>Habitatul Bizonului</h1>
        <p>{text}</p>
        <p><a href="/bizon">Înapoi la Bizon</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)
