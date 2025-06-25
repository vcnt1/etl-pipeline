import os
import sys

import pandas as pd
from tasks.transformar import Transformer


def transform():
    df = Transformer().transform(pd.read_csv(sys.argv[1]))
    df.to_csv(os.getcwd() + "/data/stage.csv")


if __name__ == "__main__":
    transform()
