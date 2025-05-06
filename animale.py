from flask import Flask
from app.lib.alimentatie import get_alimentatie
from app.lib.culoare import get_culoare

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
	<h2>Student: Chirtoaca Andreea </h2>
	<h3>Grupa: 441D</h3>
        <p><a href="/panda">Afla mai multe despre Panda</a></p>
        <p><a href="/panda/alimentatie">Hrana Panda</a></p>
        <p><a href="/panda/culoare">Culoare Panda</a></p>
    '''

@app.route("/panda")
def panda():
    return '''
        <h1>Panda</h1>
        <p><a href="/panda/alimentatie">Alimentatia Panda</a></p>
        <p><a href="/panda/culoare">Culoarea Panda</a></p>
        <p><a href="/panda">Panda</a></p>
        <p><a href="/">Tema</a></p>

    '''

@app.route("/panda/alimentatie")
def panda_alimentatie():
    alimentatie = get_alimentatie()
    return f'''
        <h1>Alimentatia Panda</h1>
        <p>{alimentatie}</p>
        <p><a href="/panda">Înapoi la Panda</a></p>
        <p><a href="/panda/culoare">Culoare Panda</a></p>
        <p><a href="/">Tema</a></p>

    '''

@app.route("/panda/culoare")
def panda_culoare():
    culoare = get_culoare()
    return f'''
        <h1>Culoarea Panda</h1>
        <p>{culoare}</p>
        <p><a href="/panda">Înapoi la Panda</a></p>
        <p><a href="/panda/alimentatie">Alimentatie Panda</a></p>
        <p><a href="/">Tema</a></p>

    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
