import pandas as pd
from logs.logger import Logger

log= Logger("etl.validator")

class Validator:
    def __init__(self):
        pass
    
    @log
    def validate(self, df: pd.DataFrame):
        # Check columns
        required_columns = ["id", "followers", "genres", "name", "popularity"]
        if not set(required_columns).issubset(set(df.columns)):
            print("invalid")
            return False
            
        # Check fields for null
        if df["name"].isnull().any():
            print("invalid")
            return False
        
        if df["followers"].isnull().any():
            print("invalid")
            return False
        
        # Check transformed Fields
        if df["popularity"].lt(1).any():
            print("invalid")
            return False
        
        return True