from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/vultur">Vultur</a></p>
    '''

@app.route("/vultur")
def vultur():
    return '''
        <h1>Vultur</h1>
        <p><a href="/vultur/descriere">Descriere</a></p>
        <p><a href="/vultur/habitat">Habitat</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/vultur/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Vulturului</h1>
        <p>{text}</p>
        <p><a href="/vultur">Înapoi la Vultur</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/vultur/habitat")
def habitat():
    text = get_habitat()
    return f'''
        <h1>Culoarea Vulturului</h1>
        <p>{text}</p>
        <p><a href="/vultur">Înapoi la Vultur</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)
