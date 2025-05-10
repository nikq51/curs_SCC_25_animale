from flask import Flask
from app.lib.arici import get_curiozitati, get_zgomot, get_emoji, get_detalii, get_intro
from app.lib.pradatori import get_pradatori

app = Flask(__name__)

nav = '''
<br><br>
<a href="/">Acasă</a> |
<a href="/despre_arici">Despre</a> |
<a href="/arici/curiozitati">Curiozități</a> |
<a href="/arici/zgomot">Zgomot</a> |
<a href="/arici/emoji">Emoji</a> |
<a href="/arici/detalii">Detalii</a> |
<a href="/arici/pradatori">Prădători</a>
'''

@app.route('/')
def home():
    return "<h1> arici 🦔!</h1>" + nav

@app.route('/despre_arici')
def intro():
    return get_intro() + nav

@app.route('/arici/curiozitati')
def curiozitati():
    return get_curiozitati() + nav

@app.route('/arici/zgomot')
def zgomot():
    return get_zgomot() + nav

@app.route('/arici/emoji')
def emoji():
    return get_emoji() + nav

@app.route('/arici/detalii')
def detalii():
    return get_detalii() + nav

@app.route('/arici/pradatori')
def pradatori():
    return get_pradatori() + nav

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
