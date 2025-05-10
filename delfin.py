from flask import Flask
from app.lib.habitat import get_habitat
from app.lib.aparitie import get_aparitie
from app.lib.sunete import get_sunete

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <html>
        <head>
            <title>Delfini</title>
            <link rel="stylesheet" href="/static/css/style.css">
        </head>
        <body>
            <h1>Tema: Animale</h1>
            <h2>Student: Petrache Andrei</h2>
            <h3>Grupa: 441D</h3>
            <p><a href="/delfin">Află mai multe despre Delfin</a></p>
        </body>
        </html>
    '''

@app.route("/delfin")
def delfin():
    return '''
        <html>
        <head>
            <title>Despre Delfini</title>
            <link rel="stylesheet" href="/static/css/style.css">
        </head>
        <body>
            <h1>Delfin</h1>
            <p><a href="/delfin/habitat">Habitat</a></p>
            <p><a href="/delfin/aparitie">Apariție</a></p>
            <p><a href="/delfin/sunete">Sunete</a></p>
            <p><a href="/">Înapoi la început</a></p>
        </body>
        </html>
    '''

@app.route("/delfin/habitat")
def delfin_habitat():
    return f'''
        <html>
        <head>
            <title>Habitat Delfin</title>
            <link rel="stylesheet" href="/static/css/style.css">
        </head>
        <body>
            <h1>Habitatul Delfinului</h1>
            <p>{get_habitat()}</p>
            <img src="/static/images/hab.jpg" alt="Habitat delfin" width="400"><br>
            <p><a href="/delfin">Înapoi la Delfin</a></p>
        </body>
        </html>
    '''

@app.route("/delfin/aparitie")
def delfin_aparitie():
    return f'''
        <html>
        <head>
            <title>Apariție Delfin</title>
            <link rel="stylesheet" href="/static/css/style.css">
        </head>
        <body>
            <h1>Apariția Delfinului</h1>
            <p>{get_aparitie()}</p>
            <img src="/static/images/delf1.jpg" alt="Apariție delfin" width="400"><br>
            <p><a href="/delfin">Înapoi la Delfin</a></p>
        </body>
        </html>
    '''

@app.route("/delfin/sunete")
def delfin_sunete():
    return f'''
        <html>
        <head>
            <title>Sunetele Delfinului</title>
            <link rel="stylesheet" href="/static/css/style.css">
        </head>
        <body>
            <h1>Sunetele Delfinului</h1>
            <p>{get_sunete()}</p>
            <img src="/static/images/com.jpg" alt="Sunete delfin" width="400"><br>
            <p><a href="/delfin">Înapoi la Delfin</a></p>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
