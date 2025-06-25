import os

import pandas as pd

from logs.logger import Logger

log = Logger("etl.transformer")


class Loader:
    def __init__(self):
        pass

    def load(self, df: pd.DataFrame, path: str):
        log.logger.info("[MOCK] Carregando dados no SQLite, ...")
        log.logger.info("[MOCK] Publicando dados via API externa, ...")
        log.logger.info("Escrevendo dados em formato .CSV, ...")
        df.to_csv(path)
