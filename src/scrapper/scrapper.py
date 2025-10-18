import pandas as pd
from datetime import datetime

from scrapper.br_investing import SITEMAP_URL as BR_INVESTING_URL
from scrapper.br_investing import get_page as br_investing_get_page, extract_news as br_investing_extract_news

from scrapper.bcb import USD_BRL_CODE as BCB_USD_BRL_CODE, SELIC_CODE as BCB_SELIC_CODE
from scrapper.bcb import get_data as bcb_get_data, get_date_range as bcb_get_date_range

from logs.logger import Logger

log = Logger("etl.scrapper")

class Scrapper():
    def __init__(self):
        pass

    def get_news(self) -> pd.DataFrame:
        min_news = 100
        news = []
        page = 1

        while len(news) < min_news:
            url = BR_INVESTING_URL
            if page > 1:
                url += f"/{page}"

            log.logger.info(f"📄 Collecting page: {url}")
            soup = br_investing_get_page(url)
            if not soup:
                raise Exception(f"Failed to get page content")
            
            items = br_investing_extract_news(soup)
            if len(items) == 0:
                log.logger.info("Breaking loop as no news were extracted")
                break

            news.extend(items)
            page += 1

        df = pd.DataFrame(news)
        df["collected_at"] = datetime.now()

        log.logger.info(f"✅ Total of news scrapped: {len(df)}")

        return df
    
    def get_monetary_history(self) -> pd.DataFrame:
        return self.get_history(BCB_USD_BRL_CODE)
    
    def get_selic_history(self) -> pd.DataFrame:
        return self.get_history(BCB_SELIC_CODE)
        
    def get_history(self, code: str) -> pd.DataFrame:
        months_back = 1
        start, end = bcb_get_date_range(months_back)

        data = bcb_get_data(code, start, end)

        # data['data'] = pd.to_datetime(data['data'], dayfirst=True)
        # data['valor'] = data['valor'].astype(float)
        return pd.DataFrame(data)
