import os
import pandas as pd
from logs.logger import Logger

log = Logger("etl.transformer")


class Transformer:
    def __init__(self):
        self.validator = Validator()

    @log
    def __drops(self, df: pd.DataFrame):
        df = df.drop_duplicates()
        df = df.drop(df[df.popularity < 1].index)
        df = df.drop(df[df.genres == "[]"].index)
        df = df.dropna(subset="followers")
        df = df.dropna(subset="name")
        return df

    @log
    def __parse_data(self, df: pd.DataFrame):
        df.genres = df.genres.str.strip("[]")
        df.genres = df.genres.str.strip()
        df.genres = df.genres.str.split(",")
        df.followers = df.followers.astype(int)
        return df

    @log
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.__drops(df)
        df = self.__parse_data(df)

        if not self.validator.is_valid(df):
            raise Exception("Falha ao validar dataframe transformado")

        return df


class Validator:
    def __init__(self):
        pass

    @log
    def is_valid(self, df: pd.DataFrame):
        required_columns = ["id", "followers", "genres", "name", "popularity"]
        if not set(required_columns).issubset(set(df.columns)):
            log.logger.error("Falha ao validate colunas obrigatórias, finalizando...")
            return False

        if df["name"].isnull().any():
            log.logger.error(
                "Valor vazio encontrado para coluna 'name', finalizando..."
            )
            return False

        if df["followers"].isnull().any():
            log.logger.error(
                "Valor vazio encontrado para coluna 'followers', finalizando..."
            )
            return False

        if df["popularity"].lt(1).any():
            log.logger.error(
                "Valor menor que 1 encontrado para coluna 'popularity', finalizando..."
            )
            return False

        return True
