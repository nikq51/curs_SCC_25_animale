from flask import Flask
app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-dark: #121212;
            --bg-light: #ffffff;
            --card-dark: #1e1e1e;
            --card-light: #f4f4f4;
            --text-dark: #e0e0e0;
            --text-light: #222222;
            --accent: #03dac5;
        }}
        body {{
            font-family: 'Poppins', sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-dark);
            margin: 0;
            transition: all 0.3s ease;
        }}
        body.light {{
            background-color: var(--bg-light);
            color: var(--text-light);
        }}
        .navbar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: rgba(30,30,30,0.9);
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            z-index: 1000;
        }}
        .navbar.light {{
            background-color: rgba(255,255,255,0.95);
        }}
        .navbar a {{
            color: var(--accent);
            font-weight: bold;
            text-decoration: none;
        }}
        .toggle-btn {{
            background: none;
            border: 1px solid var(--accent);
            color: var(--accent);
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
        }}
        .container {{
            max-width: 700px;
            margin: 120px auto 60px;
            padding: 40px;
            background-color: var(--card-dark);
            border-radius: 20px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
            text-align: center;
            transition: all 0.3s ease;
        }}
        body.light .container {{
            background-color: var(--card-light);
        }}
        button {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            color: inherit;
            padding: 14px 28px;
            margin: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }}
        button:hover {{
            background: rgba(255, 255, 255, 0.2);
            transform: scale(1.05);
        }}
        a {{
            display: inline-block;
            margin: 12px;
            text-decoration: none;
            color: var(--accent);
            font-weight: 600;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin: 6px 0;
            font-size: 17px;
        }}
        img {{
            border-radius: 12px;
            margin: 20px 0;
            max-width: 100%;
            height: auto;
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }}
    </style>
</head>
<body>
    <div class="navbar" id="navbar">
        <a href="/">🐶 Câinele Teddy</a>
        <button class="toggle-btn" onclick="toggleMode()">Light/Dark</button>
    </div>
    <div class="container">
        {continut}
    </div>
    <script>
        function toggleMode() {{
            document.body.classList.toggle('light');
            document.getElementById('navbar').classList.toggle('light');
        }}
    </script>
</body>
</html>
"""

@app.route("/", methods=['GET'])
def pagina_principala():
    continut = """
    <h1>Bine ai venit!</h1>
    <p>Aceasta este o aplicație simplă dedicată câinilor. Vei descoperi informații despre aspect, nume și trăsături simpatice.</p>
    <form action="/caine">
         <button type="submit">Explorează</button>
    </form>
    """
    return html_template.format(titlu="Acasă", continut=continut)

@app.route("/caine", methods=['GET'])
def pagina_caine():
    continut = """
    <h1>Îți prezentăm un câine adorabil!</h1>
    <img src="https://placedog.net/500/300?id=1" alt="Câine simpatic">
    <form action="/caine/descriere">
         <button type="submit">Află mai multe</button>
    </form>
    <form action="/caine/culoare">
         <button type="submit">Culoare</button>
    </form>
    """
    return html_template.format(titlu="Câine", continut=continut)

@app.route("/caine/descriere", methods=['GET'])
def descriere_caine():
    continut = """
    <h2>Descriere</h2>
    <img src="https://placedog.net/500/300?id=2" alt="Câine pufos">
    <p>Acest câine este mic, alb și foarte pufos. Are un temperament blând și jucăuș. Seamănă cu o oiță!</p>
    <form action="/caine/descriere/nume">
         <button type="submit">Vezi nume</button>
    </form>
    <a href='/caine'>← Înapoi</a>
    """
    return html_template.format(titlu="Descriere Câine", continut=continut)

@app.route("/caine/culoare", methods=['GET'])
def culoare_caine():
    continut = """
    <h2>Culoare</h2>
    <img src="https://placedog.net/500/300?id=3" alt="Câine alb">
    <p>Culoarea predominantă a acestui câine este alb imaculat. Ochii sunt căprui și expresivi.</p>
    <a href='/caine'>← Înapoi</a>
    """
    return html_template.format(titlu="Culoare Câine", continut=continut)

@app.route("/caine/descriere/nume", methods=['GET'])
def nume_caine():
    continut = """
    <h2>Nume populare pentru câini</h2>
    <img src="https://placedog.net/500/300?id=4" alt="Câine jucăuș">
    <ul>
        <li>Teddy</li>
        <li>Max</li>
        <li>Luna</li>
        <li>Daisy</li>
        <li>Rex</li>
        <li>Bella</li>
        <li>Moț</li>
    </ul>
    <a href='/caine/descriere'>← Înapoi la descriere</a>
    <a href='/caine'>← Înapoi la câine</a>
    """
    return html_template.format(titlu="Nume Câini", continut=continut)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
