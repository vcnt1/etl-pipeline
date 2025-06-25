# etl-pipeline

## Get started

This project requires:
 - python3.13

### Setup project
In order to get started, run following setup

    //on linux
    python3.13 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    export PYTHONPATH=\$PYTHONPATH:/$(pwd)
    
<br/>

    //on windows
    python3.13 -m venv .venv
    .venv\Scripts\activate.bat  
    pip install -r requirements.txt
    $env:PYTHONPATH = "$env:PYTHONPATH;$PWD"

### Update requirements.txt

To update requirements.txt:

    pip freeze > requirements.txt

## Run

To run the pipeline (after activate venv and installing dependencies):

    dvc repro

Or

    python src/main.py
