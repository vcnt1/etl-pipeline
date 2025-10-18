import duckdb
import pandas as pd

from logs.logger import Logger

log = Logger("etl.transformer")


class Loader:
    def __init__(self):
        log.logger.info("Connecting to duckDB...")
        self.conn = duckdb.connect("data/financial_data.duckdb")

    def close(self):
        self.conn.close()

    def __temp_table(self, table: str) -> str:
        return f"temp_{table}"

    def __create_schema(self, table: str, df: pd.DataFrame):
        self.conn.register(self.__temp_table(table), df)
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {table} AS SELECT * FROM temp_{table}")

    def load_news(self, df: pd.DataFrame):
        self.write_df("news", df)

    def load_monetary_history(self, df: pd.DataFrame):
        self.write_df("monetary_history", df)

    def load_selic_history(self, df: pd.DataFrame):
        self.write_df("selic_history", df)

    def write_df(self, table: str, df: pd.DataFrame):
        log.logger.info("Loading dataframe to duckDB...")
        
        self.__create_schema(table, df)

        self.conn.execute(f"INSERT INTO {table} SELECT * FROM {self.__temp_table(table)}")

        log.logger.info("Succesfully loaded data to duckDB!")

        result = self.conn.execute(f"SELECT * FROM {table} LIMIT 10").df()
        log.logger.info(result)
