import os
from pathlib import Path

import pandas as pd

from tasks.extrair import Extractor
from tasks.transformar import Transformer
from tasks.carregar import Loader
from logs.logger import Logger

log = Logger("etl.transformer")


class Pipeline:
    def __init__(self, force_extract: bool = False):
        self.extractor = Extractor()
        self.transformer = Transformer()
        self.loader = Loader()

        self.data_dir = os.getcwd() + "/data/"
        self.input_data_path = self.data_dir + "/input.csv"
        self.stage_data_path = self.data_dir + "/stage.csv"
        self.output_data_path = self.data_dir + "/output.csv"

        self.__force_extract = force_extract

    def run(self):
        log.logger.info("Iniciando ETL pipeline")

        if not self.__force_extract and not Path(self.input_data_path).is_file():
            log.logger.info("Etapa: Extração")

            df = self.extractor.extract()
            df.to_csv(self.input_data_path)
        else:
            log.logger.info("Arquivo de entrada encontrado, pulando extração...")

            df = pd.read_csv(self.input_data_path)

        log.logger.info("Etapa: Transformação")

        df = self.transformer.transform(df)
        df.to_csv(self.stage_data_path)

        log.logger.info("Etapa: Carregamento")

        df = self.loader.load(df, self.output_data_path)

        log.logger.info("ETL pipeline finalizada com sucesso!")
