import os
from tasks.extrair import Extractor


def extract():
    df = Extractor().extract()
    df.to_csv(os.getcwd() + "/data/input.csv")


if __name__ == "__main__":
    extract()
