
import pandas as pd
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from logs.logger import Logger

log= Logger("etl.transformer")

class Transformer:
    def __init__(self):
        pass
    
    @log
    def __drops(self, df: pd.DataFrame):
        df = df.drop_duplicates()
        df = df.drop(df[df.popularity < 1].index)
        df = df.drop(df[df.genres == '[]'].index)
        df = df.dropna(subset='followers')
        df = df.dropna(subset='name')
        return df
    
    @log
    def __parse_data(self, df: pd.DataFrame):
        # data transformations
        df.genres = df.genres.str.strip("[]")
        df.genres = df.genres.str.strip()
        df.genres = df.genres.str.split(",")
        df.followers = df.followers.astype(int)
        return df

    @log
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.__drops(df)
        df = self.__parse_data(df)
        return df
