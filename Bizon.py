from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/nevastuica">Nevastuica</a></p>
    '''

@app.route("/nevastuica")
def nevastuica():
    return '''
        <h1>Nevastuica</h1>
        <p><a href="/nevastuica/descriere">Descriere</a></p>
        <p><a href="/nevastuica/habitat">Habitat</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/nevastuica/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Nevastuicii</h1>
        <p>{text}</p>
        <p><a href="/nevastuica">Înapoi la Nevastuica</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/nevastuica/habitat")
def habitat():
    text = get_habitat()
    return f'''
        <h1>Habitatul Nevastuicii</h1>
        <p>{text}</p>
        <p><a href="/nevastuica">Înapoi la Nevastuica</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)
