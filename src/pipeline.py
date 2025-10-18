from tasks.extractor import Extractor
from tasks.transformer import Transformer
from tasks.loader import Loader

from logs.logger import Logger

log = Logger("etl.transformer")


class Pipeline:
    def __init__(self):
        self.extractor = Extractor()
        self.transformer = Transformer()
        self.loader = Loader()


    def run(self):
        log.logger.info("Starting ETL pipeline")

        df = self.extractor.collect_news()
        self.loader.load_news(df)

        df = self.extractor.collect_monetary_history()
        self.loader.load_monetary_history(df)

        df = self.extractor.collect_selic_history()
        df_t = self.transformer.bcb_selic_to_history_series(df)
        self.loader.load_selic_history(df_t)

        log.logger.info("ETL pipeline finished successfully!")

        log.logger.info("Closing dependencies...")
        self.loader.close()
