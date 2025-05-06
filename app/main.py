from flask import Flask
from app.lib.biblioteca_animale import culoare_alpaca, descriere_alpaca

app = Flask(__name__)

@app.route('/alpaca')
def pagina_alpaca():
    return "Bine ați venit la pagina Alpaca!"

@app.route('/culoare_alpaca')
def ruta_culoare():
    return culoare_alpaca()

@app.route('/descriere_alpaca')
def ruta_descriere():
    return descriere_alpaca()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
