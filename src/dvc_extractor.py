import os
from tasks.extractor import Extractor


def extract():
    extractor = Extractor()

    df = extractor.collect_news()
    df.to_parquet(os.getcwd() + "/data/brinvesting_news_stage.parquet")

    df = extractor.collect_monetary_history()
    df.to_parquet(os.getcwd() + "/data/bcb_real2dolar_stage.parquet")


    df = extractor.collect_selic_history()
    df.to_parquet(os.getcwd() + "/data/bcb_selic_input.parquet")


if __name__ == "__main__":
    extract()
