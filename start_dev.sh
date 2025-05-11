#!/bin/bash

echo "[INFO] Activare mediu virtual..."
source venv/bin/activate

echo "[INFO] Setare PYTHONPATH..."
export PYTHONPATH=$(pwd)

if ! pip show flask > /dev/null 2>&1; then
    echo "[INFO] Instalare dependințe din quickrequirements.txt..."
    pip install -r quickrequirements.txt
else
    echo "[INFO] Dependențele sunt deja instalate."
fi

echo "[INFO] Verificare cod cu pylint..."
pylint tigru.py app/lib/*.py app/tests/*.py || true

echo "[INFO] Rulare teste cu pytest..."
pytest app/tests -v

echo "[INFO] Gata. Totul a fost verificat."
