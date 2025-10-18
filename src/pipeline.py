import pandas as pd

from tasks.extractor import Extractor
from tasks.transformer import Transformer
from tasks.loader import Loader
from logs.logger import Logger

log = Logger("etl.transformer")


class Pipeline:
    def __init__(self):
        self.extractor = Extractor()
        self.loader = Loader()


    def run(self):
        log.logger.info("Starting ETL pipeline")

        df = self.extractor.collect_news()
        # df = pd.read_csv("news.csv")
        self.loader.load_news(df)

        df = self.extractor.collect_monetary_history()
        self.loader.load_monetary_history(df)

        df = self.extractor.collect_selic_history()
        self.loader.load_selic_history(df)

        log.logger.info("ETL pipeline finished successfully!")

        log.logger.info("Closing dependencies...")
        self.loader.close()
