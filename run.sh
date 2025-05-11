#!/bin/bash
export PYTHONPATH=$(pwd)
export FLASK_APP=app/main.py
flask run
pytest
