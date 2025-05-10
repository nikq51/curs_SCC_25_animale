from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bine ai venit in aplicatie Lemur!</h1>"

@app.route("/lemur")
def lemur():
    return '''<h2>Pagina animalului Lemur</h2>
<ul>
    <li><a href="/lemur/culoare">Culoare</a></li>
    <li><a href="/lemur/descriere">Descriere</a></li>
</ul>
'''

@app.route("/lemur/culoare")
def culoare():
    return "Lemurul are blana gri cu coada dungata."

@app.route("/lemur/descriere")
def descriere():
    return "Lemurul este un primat originar din Madagascar, activ mai ales noaptea."

