# etl-pipeline

# 🧠 Fintech Data Pipeline — Market & Macro Data ETL

This project implements a **data engineering pipeline** for a **Fintech investment platform**, designed to enrich its analytical data warehouse with **public market and macroeconomic data**.

It supports **web scraping of financial news**, **collection of historical economic series**, and **storage in a local DuckDB database** for downstream analytics and dashboards.

---

## 🚀 Features

- 📰 **Web Scraper** using `requests`, `BeautifulSoup` and `Selenium`
  - Collects financial news (title, date, lead, and URL)
  - Fully compliant with site `robots.txt` rules
  - Supports headless scraping for better performance and stealth

- 📈 **Public APIs Integration**
  - **Banco Central do Brasil (SGS API)** for macroeconomic time series  
    - Exchange rates (USD/BRL)
    - SELIC interest rate

- 🪶 **Data Persistence with DuckDB**
  - Fast, file-based analytical database
  - Ideal for local analytics and integration with tools like Power BI or Tableau
  - Easy ingestion from Pandas DataFrames


## Get started

This project requires:
 - python3.13

### Setup project
In order to get started, run following setup

    python3.13 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    export PYTHONPATH=\$PYTHONPATH:/$(pwd)

### Update requirements.txt

To update requirements.txt:

    pip freeze > requirements.txt

## Run

To run the pipeline (after setting everything up):

    dvc repro

Or

    python src/main.py

## Known problems and limtiation
TODOs:
  - Add support to fetch BCB data for more than 120 months(10 years);
  - Fetch news' lead;

Bugs:
  - Jupyter notebook is not able to persist on Duckdb local file;
