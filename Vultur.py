from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.habitat import get_habitat

app = Flask(__name__)

def pagina(titlu, continut):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}
            .container {{
                background-color: #ffffff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                max-width: 600px;
                width: 100%;
                text-align: center;
            }}
            h1 {{
                color: #2c3e50;
                margin-bottom: 20px;
            }}
            .btn {{
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                transition: background-color 0.2s;
            }}
            .btn:hover {{
                background-color: #2980b9;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {continut}
        </div>
    </body>
    </html>
    """

@app.route("/")
def index():
    return pagina("Animale", """
        <h1>Tema: Animale</h1>
        <a href="/vultur" class="btn">🦅 Vultur</a>
    """)

@app.route("/vultur")
def vultur():
    return pagina("Vultur", """
        <h1>Vultur</h1>
        <a href="/vultur/descriere" class="btn">📄 Descriere</a>
        <a href="/vultur/habitat" class="btn">🌍 Habitat</a>
        <a href="/" class="btn">🏠 Acasa</a>
    """)

@app.route("/vultur/descriere")
def descriere():
    text = get_descriere()
    return pagina("Descriere Vultur", f"""
        <h1>Descrierea Vulturului</h1>
        <p>{text}</p>
        <a href="/vultur" class="btn">🔙 Inapoi la Vultur</a>
        <a href="/" class="btn">🏠 Pagina principala</a>
    """)

@app.route("/vultur/habitat")
def habitat():
    text = get_habitat()
    return pagina("Habitat Vultur", f"""
        <h1>Habitatul Vulturului</h1>
        <p>{text}</p>
        <a href="/vultur" class="btn">🔙 Inapoi la Vultur</a>
        <a href="/" class="btn">🏠 Pagina principala</a>
    """)

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)

