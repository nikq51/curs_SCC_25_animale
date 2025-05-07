# curs_vcgj_25_441_animale -> pisica.py

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
2. [Descriere versiune](#descriere-versiune)
3. [Configurare](#configurare)
4. [Exemple pagina web](#exemple-pagina-web)
5. [Testare cu pytest](#testare-cu-pytest)
6. [Verificare statica. pylint](#verificare-statica-cu-pylint)
7. [Bibliografie](#bibliografie)

# Descriere aplicatie

Aplicatia pisica.py este o aplicatie web simpla scrisa in Python folosind framework-ul Flask, care simuleaza o mica aventura interactiva in lumea pisicilor. Utilizatorul poate naviga prin pagini HTML stilizate ce afiseaza informatii despre o pisica, precum descrierea, culoarea si nume amuzante.

Aplicatia este modularizata si organizata in foldere app/lib, app/tests, oferind si o componenta de testare unitara cu pytest, dar si verificare statica a codului cu pylint.

Aplicatia poate fi containerizata cu Docker si integrata in pipeline-uri Jenkins pentru testare si build automat.

# Descriere versiune
# v1.0 - prima versiune

* ruta principala '/' - [http://127.0.0.1:5050](http://127.0.0.1:5050)
* rute aditionale:
  * '/pisica' - pagina "home" cu poza si butoane
  * '/pisica/descriere' - descrierea pisicii
  * '/pisica/culoare' - culoarea pisicii
  * '/pisica/descriere/nume' - lista cu nume de pisici

# Configurare

Aplicatia se bazeaza pe un mediu virtual si necesita instalarea dependintelor:

python3 -m venv .venv                  -> creeaza un mediu virtual Python in folderul .venv

source .venv/bin/activate              -> activeaza mediul virtual

pip install -r quickrequirements.txt   -> instaleaza toate bibliotecile din fisierul quickrequirements.txt

python pisica.py                       -> porneste aplicatia pisica.py

Serverul porneste pe IP: 127.0.0.1 si port 5050. Acces server din browser: http://127.0.0.1:5050

# Exemple pagina web

## Pagina principala

* Afișează un mesaj de bun venit și un buton de acces către pagina "pisica".

## Pagina "pisica"

* Afiseaza două butoane catre alte rute: Descriere și Culoare.

## Pagina descriere

* Afișează un text cu descrierea pisicii și un buton pentru afișarea unor nume simpatice.

## Pagina culoare

* Afișează informații despre culoarea pisicii și un link de întoarcere la pagina principala.

## Pagina nume

* Afișează lista de nume amuzante pentru pisici.

# Testare cu pytest

Testele sunt plasate in app/tests/ si verifica:

* Functionalitatea functiilor helper (din app/lib/helper.py)
* Raspunsul generat de rutele principale (/, /pisica, etc.)

# Verificare statica cu pylint

-> pylint - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
-> in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

pylint pisica.py app/lib/*.py app/tests/*.py

# Bibliografie

* https://github.com/crchende/sysinfo
* https://www.jenkins.io/
* https://docs.docker.com/
