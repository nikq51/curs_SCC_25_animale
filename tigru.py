from flask import Flask

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <style>
        body {{
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #2f2f2f;
            color: #eae0d5;
            text-align: center;
        }}
        .header {{
            background-color: #3b3b3b;
            padding: 20px 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }}
        .app-title {{
            color: #c97c32;
            font-size: 36px;
            letter-spacing: 2px;
            font-family: 'Georgia', serif;
            margin: 0;
        }}
        .container {{
            background-color: #3e3e3e;
            padding: 40px;
            border-radius: 10px;
            width: 70%;
            margin: 30px auto;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
        }}
        h1 {{
            font-size: 28px;
            color: #d6a96c;
            margin-bottom: 20px;
        }}
        p {{
            font-size: 18px;
            color: #eae0d5;
            line-height: 1.6;
            margin-bottom: 30px;
        }}
        img {{
            border: 4px solid #c97c32;
            border-radius: 8px;
            margin-bottom: 20px;
            max-width: 100%;
            height: auto;
        }}
        .btn {{
            background: linear-gradient(45deg, #ff5722, #e65100);
            color: white;
            padding: 14px 30px;
            margin: 10px;
            border: 2px solid #ff9800;
            border-radius: 30% 70% 30% 70% / 50% 40% 60% 50%;
            text-decoration: none;
            font-weight: bold;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(255, 87, 34, 0.5);
        }}
        .btn:hover {{
            background: #ff9800;
            color: #212121;
            transform: scale(1.05) rotate(-1deg);
        }}
    </style>
</head>
<body>
    <header class="header">
        <h1 class="app-title">🐅 Tigrul Sălbatic</h1>
    </header>
    <div class="container">
        {continut}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    continut = """
    <h1>Intră în teritoriul tigrului</h1>
    <p>Nu e grădina zoologică. E jungla. Și tu tocmai ai pășit în mijlocul ei.<br>
    Doar cei curajoși merg mai departe.</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg" width="350" alt="Tigru Sălbatic">
    <br><br>
    <a href="/descriere" class="btn">Vezi descrierea</a>
    <a href="/culoare" class="btn">Vezi culoarea</a>
    """
    return html_template.format(titlu="Tigru Sălbatic", continut=continut)

@app.route("/descriere")
def descriere():
    continut = """
    <h1>Descrierea tigrului</h1>
    <p>Tigrul este un vânător solitar, cu o forță și agilitate uluitoare.<br>
    Trăiește în junglele dese și e simbolul puterii neîmblânzite.</p>
    <a href="/" class="btn">Înapoi</a>
    """
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/culoare")
def culoare():
    continut = """
    <h1>Culoarea tigrului</h1>
    <p>Blana portocalie intensă, cu dungi negre perfect simetrice.<br> 
    Ochii săi — verzi sau aurii — par că te privesc prin suflet.</p>
    <a href="/" class="btn">Înapoi</a>
    """
    return html_template.format(titlu="Culoare", continut=continut)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
