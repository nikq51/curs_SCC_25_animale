from flask import Flask
from app.lib.descriere_marmota import get_descriere
from app.lib.mancare_marmota import get_mancare_marmota

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/marmota">Marmota</a></p>
    '''

@app.route("/marmota")
def marmota():
    return '''
        <h1>Marmota</h1>
        <p><a href="/marmota/descriere_marmota">Descriere</a></p>
        <p><a href="/marmota/mancare_marmota">Mancare</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/marmota/descriere_marmota")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descriere Marmota</h1>
        <p>{text}</p>
        <p><a href="/marmota">Înapoi la Marmota</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/marmota/mancare_marmota")
def mancare():
    text = get_mancare_marmota()
    return f'''
        <h1>Mancare Marmota</h1>
        <p>{text}</p>
        <p><a href="/marmota">Înapoi la Marmota</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

