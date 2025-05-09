from flask import Flask

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <style>
        * {{
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Verdana', sans-serif;
            background-color: #fff9e6;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #f1c40f;
            color: #2c3e50;
            padding: 20px 30px;
            font-size: 24px;
            font-weight: bold;
        }}
        .container {{
            max-width: 800px;
            margin: 30px auto;
            padding: 30px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }}
        h1, h2 {{
            color: #2c3e50;
            margin-top: 0;
        }}
        p {{
            color: #444;
            font-size: 16px;
        }}
        .btn {{
            display: inline-block;
            background-color: #f1c40f;
            color: #2c3e50;
            padding: 12px 24px;
            margin: 10px 5px 0 0;
            border: none;
            border-radius: 4px;
            text-decoration: none;
            font-size: 15px;
            transition: background-color 0.3s ease;
        }}
        .btn:hover {{
            background-color: #d4ac0d;
        }}
        .link {{
            display: inline-block;
            margin-top: 20px;
            font-size: 14px;
            color: #b7950b;
            text-decoration: none;
        }}
        .link:hover {{
            text-decoration: underline;
        }}
        img {{
            max-width: 100%;
            border-radius: 8px;
            margin: 20px 0;
        }}
        ul {{
            text-align: left;
            padding-left: 20px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <header>Puma Explorer</header>
    <div class="container">
        {continut}
    </div>
</body>
</html>
"""

@app.route("/", methods=['GET'])
def pagina_principala():
    continut = """
    <h1>Bine ai venit!</h1>
    <p>Explorează lumea misterioasă a pumei — un prădător elegant și puternic.</p>
    <form action="/puma">
        <button class="btn" type="submit">Intră în lumea Puma</button>
    </form>
    """
    return html_template.format(titlu="Start", continut=continut)

@app.route("/puma", methods=['GET'])
def pagina_puma():
    continut = """
    <h1>Faceți cunoștință cu Puma</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Cougar_closeup.jpg/640px-Cougar_closeup.jpg" alt="Puma"><br>
    <form action="/puma/descriere">
         <button class="btn" type="submit">Descriere Puma</button>
    </form>
    <form action="/puma/culoare">
         <button class="btn" type="submit">Culoare Puma</button>
    </form>
    """
    return html_template.format(titlu="Puma", continut=continut)

@app.route("/puma/descriere", methods=['GET'])
def descriere_puma():
    continut = """
    <h2>Despre Puma</h2>
    <p>Puma este un mamifer solitar, foarte agil și adaptabil, care trăiește în diferite tipuri de habitate.</p>
    <form action="/puma/descriere/locatii">
         <button class="btn" type="submit">Unde trăiește Puma?</button>
    </form>
    <a class="link" href='/puma'>← Înapoi</a>
    """
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/puma/culoare", methods=['GET'])
def culoare_puma():
    continut = """
    <h2>Puma are o blană cafenie-aurie cu tonuri deschise pe abdomen și piept.</h2>
    <a class="link" href='/puma'>← Înapoi</a>
    """
    return html_template.format(titlu="Culoare Puma", continut=continut)

@app.route("/puma/descriere/locatii", methods=['GET'])
def locatii_puma():
    continut = """
    <h2>Zone unde trăiește puma în sălbăticie:</h2>
    <ul>
        <li>Munții Anzi (America de Sud)</li>
        <li>Munții Stâncoși (SUA și Canada)</li>
        <li>Pădurile din America Centrală</li>
        <li>Regiunile deșertice din sud-vestul SUA</li>
        <li>Platourile din Patagonia</li>
    </ul>
    <div>
        <a class="link" href='/puma/descriere'>← Înapoi la descriere</a>
        <a class="link" href='/puma'>← Înapoi la pagina principală</a>
    </div>
    """
    return html_template.format(titlu="Habitat Puma", continut=continut)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
