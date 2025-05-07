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
            font-family: 'Trebuchet MS', sans-serif;
            background: linear-gradient(135deg, #1b5e20, #33691e);
            color: #fff;
            text-align: center;
            padding: 0;
        }}
        .header {{
            background-color: #1b1b1b;
            padding: 20px 0;
            margin-bottom: 30px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }}
        .app-title {{
            color: #ff9800;
            font-size: 36px;
            letter-spacing: 3px;
            margin: 0;
            font-family: 'Impact', sans-serif;
        }}
        .container {{
            background-color: rgba(0, 0, 0, 0.4);
            padding: 40px;
            border-radius: 15px;
            width: 60%;
            margin: auto;
            box-shadow: 0 0 25px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-size: 30px;
            color: #ff9800;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }}
        p {{
            font-size: 18px;
            color: #f1f8e9;
            margin-bottom: 30px;
        }}
        img {{
            border: 5px solid #ff9800;
            border-radius: 10px;
            margin-bottom: 20px;
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
        <h1 class="app-title">🐅 Tigrul Sălbatic 🐅</h1>
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
    <p>Tigrul este un vânător solitar, cu o forță și agilitate uluitoare. 
    Mișcarea lui este silențioasă, iar privirea — mortală.<br>
    Trăiește în junglele dese și e simbolul puterii neîmblânzite.</p>
    <a href="/" class="btn">Înapoi</a>
    """
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/culoare")
def culoare():
    continut = """
    <h1>Culoarea tigrului</h1>
    <p>Blana portocalie intensă, cu dungi negre perfect simetrice, 
    îi oferă camuflaj în vegetația deasă.<br> 
    Ochii săi — verzi sau aurii — par că te privesc prin suflet.</p>
    <a href="/" class="btn">Înapoi</a>
    """
    return html_template.format(titlu="Culoare", continut=continut)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
