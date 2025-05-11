from flask import Flask, render_template_string
from app.lib.biblioteca_animale import culoare_veverita, descriere_veverita

app = Flask(__name__)

style = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    .container {
        max-width: 600px;
        margin: 100px auto;
        padding: 30px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #333;
        margin-bottom: 30px;
    }
    a {
        display: block;
        margin: 10px 0;
        text-decoration: none;
        color: #0066cc;
        font-weight: bold;
    }
    a:hover {
        color: #003d99;
    }
    p {
        font-size: 18px;
        color: #444;
    }
</style>
"""

@app.route('/veverita')
def pagina_veverita():
    html = f"""
    {style}
    <div class="container">
        <h1>Bine ați venit la pagina veveriței!</h1>
        <a href="/culoare_veverita">Vezi culoarea veveriței</a>
        <a href="/descriere_veverita">Vezi descrierea veveriței</a>
    </div>
    """
    return render_template_string(html)

@app.route('/culoare_veverita')
def ruta_culoare():
    html = f"""
    {style}
    <div class="container">
        <p>{culoare_veverita()}</p>
        <a href="/veverita">&larr; Înapoi</a>
    </div>
    """
    return render_template_string(html)

@app.route('/descriere_veverita')
def ruta_descriere():
    html = f"""
    {style}
    <div class="container">
        <p>{descriere_veverita()}</p>
        <a href="/veverita">&larr; Înapoi</a>
    </div>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

