
import argparse
import os
import warnings

import pandas as pd
from etl.transformer import Transformer
from etl.validator import Validator
import kagglehub
from kagglehub import KaggleDatasetAdapter
from logs.logger import Logger

transformer = Transformer()
validator = Validator()
log= Logger()

@log
def download():
    # hide kaggle depecrated warning
    warnings.filterwarnings("ignore")
    
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "nimishasen27/spotify-dataset",
        "artists.csv",)
    
    # turn warning on again
    warnings.filterwarnings("default")
    
    current_directory = os.getcwd()
    path = current_directory + "/data/base_dataset.csv"
    df.to_csv(path)

@log
def transform():
    current_directory = os.getcwd()
    read_path = current_directory + "/data/base_dataset.csv"
    df = pd.read_csv(read_path)
    df = transformer.transform(df)
    current_directory = os.getcwd()
    path = current_directory + "/data/transformed_dataset.csv"
    df.to_csv(path)
    
@log
def validate():
    current_directory = os.getcwd()
    read_path = current_directory+"/data/transformed_dataset.csv"
    df = pd.read_csv(read_path)
    valid = validator.validate(df)
    if not valid:
        return
    
    # Set dataset as validated
    os.rename(read_path, current_directory+"/data/transformed_dataset_validated.csv")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--etapa", choices=["download", "transform", "validate"], required=True)
    args = parser.parse_args()

    if args.etapa == "download":
        download()
    elif args.etapa == "transform":
        transform()
    elif args.etapa == "validate":
        validate()

if __name__ == "__main__":
    main()
