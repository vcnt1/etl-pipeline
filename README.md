# etl-pipeline

## Get started

This project requires:
 - python3.13

### Setup project
In order to get started, run following setup

    python3.13 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

### Update requirements.txt

To update requirements.txt:

    pip freeze > requirements.txt

## Run

To run the pipeline (after activate venv and installing dependencies):

    dvc repro

Or
    python src/main.go
