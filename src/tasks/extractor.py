import pandas as pd

from logs.logger import Logger
from scrapper.scrapper import Scrapper

log = Logger("etl.extractor")


class Extractor:
    def __init__(self):
        self.scrapper = Scrapper()

    def collect_news(self) -> pd.DataFrame:
        return self.scrapper.get_news()
    
    def collect_monetary_history(self) -> pd.DataFrame:
        return self.scrapper.get_monetary_history()
    
    def collect_selic_history(self) -> pd.DataFrame:
        return self.scrapper.get_selic_history()
