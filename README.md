
# curs_vcgj_25_441_animale

# `caine`
===================================

# Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Descriere versiune](#descriere-versiune)
   1. [Buguri cunoscute](#probleme-cunoscute)
3. [Configurare](#configurare)
4. [Exemple pagină web](#exemple-pagină-web)
5. [Testare cu pytest](#testare-cu-pytest)
6. [Verificare statică - pylint](#verificare-statică-cu-pylint)
7. [Utilizare Docker și containerizare aplicație](#utilizare-docker)
8. [DevOps - CI](#devops)
   1. [Pipeline Jenkins](#pipeline-jenkins)
9. [Bibliografie](#bibliografie)

---

# Descriere aplicație

Aplicația `caine` este o aplicație web dezvoltată cu Flask care oferă informații despre o rasă de câine. Aceasta expune mai multe rute HTTP prin care utilizatorul poate obține descrierea, culoarea și alte detalii despre câine.

Scopul aplicației este didactic, fiind folosită pentru testarea și integrarea continuă cu Jenkins, precum și pentru containerizare cu Docker.

---

# Descriere versiune

## v1.0

- Rută principală `/` care afișează un meniu simplu HTML.
- Alte rute disponibile:
  - `/caine`
  - `/caine/culoare`
  - `/caine/descriere`

## Probleme cunoscute

- Lipsa unor teste unitare detaliate pentru toate funcțiile.
- Codul poate fi îmbunătățit din punct de vedere al stilului conform pylint.

---

# Configurare

### 1. Clonare repository:

```bash
git clone https://github.com/nikq51/curs_SCC_25_animale.git
cd curs_SCC_25_animale
