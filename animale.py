from flask import Flask
from app.lib.culoare import get_culoare
from app.lib.habitat import get_habitat

app = Flask(__name__)

nav_buttons = '''
<br><br>
<a href="/">Acasă</a> |
<a href="/leu">Leu</a> |
<a href="/leu/culoare">Culoare</a> |
<a href="/leu/habitat">Habitat</a>
'''

@app.route('/')
def home():
    return f"<h1>tema grupei este ANIMALE</h1>" + nav_buttons

@app.route('/leu')
def leu():
    return f"<h1>animalul meu este LEU</h1>" + nav_buttons

@app.route('/leu/culoare')
def culoare():
    return f"<h1>Culoare Leu</h1><p>{get_culoare()}</p>" + nav_buttons

@app.route('/leu/habitat')
def habitat():
    return f"<h1>Habitate Naturale</h1><p>{get_habitat()}</p>" + nav_buttons

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
