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
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            text-align: center;
            padding: 50px;
        }}
        h1, h2 {{
            color: #333;
        }}
        .container {{
            background-color: #ffffff;
            padding: 30px;
            margin: auto;
            width: 50%;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        button {{
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
        button:hover {{
            background-color: #45a049;
        }}
        a {{
            display: inline-block;
            margin: 10px;
            text-decoration: none;
            color: #4CAF50;
            font-weight: bold;
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
@app.route("/", methods=['GET'])
def pagina_principala():
    continut = """
    <h1> Bine ai venit la lumea pisicilor!</h1>
    <p class="intro">
        Aceasta este o pagină dedicată pisicilor. Aici poți afla descrierea, culorile și numele amuzante ale pisicilor.
        Apasă pe butonul de mai jos pentru a începe aventura!
    </p>
    <form action="/pisica">
         <button type="submit">Intră în lumea pisicilor</button>
    </form>
    """
    return html_template.format(titlu="Pagina Principală", continut=continut)

@app.route("/pisica", methods=['GET'])
def pagina_pisica():
    continut = """
    <h1> Aceasta este o pisica </h1>
    <img src="https://placekitten.com/300/200" alt="Pisica draguta"><br>
    <form action="/pisica/descriere">
         <button type="submit">Descriere pisica</button>
    </form>
    <form action="/pisica/culoare">
         <button type="submit">Culoare pisica</button>
    </form>
    """
    return html_template.format(titlu="Pisica", continut=continut)

@app.route("/pisica/descriere", methods=['GET'])
def descriere_pisica():
    continut = """
    <h2> Pisica este un animal bland, curios si adorabil. </h2>
    <form action="/pisica/descriere/nume">
         <button type="submit">Nume dragute de pisici</button>
    </form>
    <a href='/pisica'>← Inapoi la pagina principala</a>
    """
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/pisica/culoare", methods=['GET'])
def culoare_pisica():
    continut = """
    <h2> Pisica este de culoare gri cu alb si are ochii verzi. </h2>
    <a href='/pisica'>← Inapoi</a>
    """
    return html_template.format(titlu="Culoare", continut=continut)

@app.route("/pisica/descriere/nume", methods=['GET'])
def nume_pisica():
    continut = """
    <h2>Nume amuzante si dragute pentru pisici:</h2>
    <ul style="text-align: left; display: inline-block;">
        <li>Mitzi</li>
        <li>Gogosica</li>
        <li>MiauMiau</li>
        <li>Smotoc</li>
        <li>Norisor</li>
        <li>Captain Whiskers</li>
        <li>Zgubi</li>
    </ul>
    <div style="margin-top: 30px;">
        <a href='/pisica/descriere'>← Inapoi la descriere</a>
        <a href='/pisica' style="margin-left: 20px;">← Inapoi la pagina principala</a>
    </div>
    """
    return html_template.format(titlu="Nume Pisici", continut=continut)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
