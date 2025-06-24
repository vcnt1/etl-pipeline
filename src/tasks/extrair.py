import os
import warnings

from logs.logger import Logger
import kagglehub
from kagglehub import KaggleDatasetAdapter

log = Logger("etl.transformer")


class Extractor:
    def __init__(self):
        pass

    def extract(self):
        # hide kaggle depecrated warning
        warnings.filterwarnings("ignore")

        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "nimishasen27/spotify-dataset",
            "artists.csv",
        )

        # turn warning on again
        warnings.filterwarnings("default")

        current_directory = os.getcwd()
        path = current_directory + "/data/input.csv"
        df.to_csv(path)
