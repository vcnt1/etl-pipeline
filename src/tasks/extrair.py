import os
import warnings

import pandas as pd

from logs.logger import Logger
import kagglehub
from kagglehub import KaggleDatasetAdapter

log = Logger("etl.transformer")


class Extractor:
    def __init__(self):
        pass

    def extract(self) -> pd.DataFrame:
        # hide kaggle depecrated warning
        warnings.filterwarnings("ignore")

        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "nimishasen27/spotify-dataset",
            "artists.csv",
        )

        # turn warning on again
        warnings.filterwarnings("default")

        return df
