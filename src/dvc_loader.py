import os
import sys
import pandas as pd
from tasks.carregar import Loader


def load():
    Loader().load(pd.read_csv(sys.argv[1]), os.getcwd() + "/data/output.csv")


if __name__ == "__main__":
    load()
