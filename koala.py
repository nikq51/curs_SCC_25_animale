from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Aplicația Koala</h1>"

@app.route("/koala")
def koala():
    return '''
    <h2>Pagina animalului Koala</h2>
    <ul>
        <li><a href="/koala/culoare">Culoare</a></li>
        <li><a href="/koala/descriere">Descriere</a></li>
    </ul>
    '''

@app.route("/koala/culoare")
def culoare():
    return "Koala este cenușiu."

@app.route("/koala/descriere")
def descriere():
    return "Koala este un mamifer marsupial din Australia."
