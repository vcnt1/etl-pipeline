import os
import sys
import pandas as pd
from tasks.loader import Loader


def load():
    loader = Loader()

    loader.load_news(pd.read_parquet(sys.argv[1]))
    loader.load_monetary_history(pd.read_parquet(sys.argv[2]))
    loader.load_selic_history(pd.read_parquet(sys.argv[3]))


if __name__ == "__main__":
    load()
