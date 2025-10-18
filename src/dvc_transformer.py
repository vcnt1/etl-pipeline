import os
import sys

import pandas as pd
from tasks.transformer import Transformer


def transform():
    transformer = Transformer()
    df = transformer.bcb_selic_to_history_series(pd.read_parquet(sys.argv[1]))
    df.to_parquet(os.getcwd() + "/data/bcb_selic_stage.parquet")


if __name__ == "__main__":
    transform()
