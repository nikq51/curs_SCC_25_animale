from flask import Flask
from app.lib.info_general import get_homepage_info, get_urs_info
from app.lib.alimentatie import get_alimentatie
from app.lib.specii import get_specii

app = Flask(__name__)

nav_buttons = '''
<br><br>
<a href="/">Acasă</a> |
<a href="/urs">Urs</a> |
<a href="/urs/alimentatie">Alimentație</a> |
<a href="/urs/specii">Specii</a>
'''

@app.route('/')
def home():
    return f"<h1>{get_homepage_info()}</h1>" + nav_buttons

@app.route('/urs')
def urs():
    return f"<h1>{get_urs_info()}</h1>" + nav_buttons

@app.route('/urs/alimentatie')
def alimentatie():
    return f"<h1>Alimentație Urs</h1><p>{get_alimentatie()}</p>" + nav_buttons

@app.route('/urs/specii')
def specii():
    return f"<h1>Specii de Urși</h1><p>{get_specii()}</p>" + nav_buttons

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
