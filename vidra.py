from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/vidra">Vidra</a></p>
    '''

@app.route("/vidra")
def capibara():
    return '''
        <h1>Vidra</h1>
        <p><a href="/vidra/descriere">Descriere</a></p>
        <p><a href="/vidra/habitat">Habitat</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/vidra/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Vidrei</h1>
        <p>{text}</p>
        <p><a href="/vidra">Înapoi la Vidra</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/vidra/habitat")
def habitat():
    text = get_habitat()
    return f'''
        <h1>Habitatul Vidrei</h1>
        <p>{text}</p>
        <p><a href="/vidra">Înapoi la Vidra</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
