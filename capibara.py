from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.culoare import get_culoare

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Animale</h1>
        <p><a href="/capibara">Capibara</a></p>
    '''

@app.route("/capibara")
def capibara():
    return '''
        <h1>Capibara</h1>
        <p><a href="/capibara/descriere">Descriere</a></p>
        <p><a href="/capibara/culoare">Culoare</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/capibara/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea Capibarei</h1>
        <p>{text}</p>
        <p><a href="/capibara">Înapoi la Capibara</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/capibara/culoare")
def culoare():
    text = get_culoare()
    return f'''
        <h1>Culoarea Capibarei</h1>
        <p>{text}</p>
        <p><a href="/capibara">Înapoi la Capibara</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

