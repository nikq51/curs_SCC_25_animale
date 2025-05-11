#!/bin/bash

# Activează venv
echo "[INFO] Activare venv..."
source venv/bin/activate

# Instalează Flask dacă nu e deja
if ! pip show flask > /dev/null 2>&1; then
    echo "[INFO] Flask nu e instalat. Îl instalez..."
    pip install flask --break-system-packages
else
    echo "[INFO] Flask este deja instalat."
fi

# Rulează aplicația
echo "[INFO] Pornesc aplicația..."
python3 tigru.py
