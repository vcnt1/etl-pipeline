import os

import pandas as pd

from logs.logger import Logger

log = Logger("etl.transformer")


class Loader:
    def __init__(self):
        pass

    def load(self, df: pd.DataFrame, path: str):
        df.to_csv(path)
