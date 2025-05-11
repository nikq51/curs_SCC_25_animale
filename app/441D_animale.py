from flask import Flask
from lib.biblioteca_animale import culoare_cal, descriere_cal

app = Flask(__name__)

@app.route('/cal')
def cal():
  return "Aceasta este pagina dedicata calului."

@app.route('/cal/culoare')
def culoare_cal():
  return  "Are culori cum ar fi negru, maro, alb sau combinatii"

@app.route('/cal/descriere')
def descriere_cal():
  return  "Este domestic"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 5000)
