#!/bin/bash

echo "[INFO] Activare mediu virtual..."
source venv/bin/activate

echo "[INFO] Setare PYTHONPATH..."
export PYTHONPATH=$(pwd)

echo "[INFO] Pornire aplicație Flask..."
python tigru.py
