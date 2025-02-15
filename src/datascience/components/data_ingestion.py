import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataIngestionConfig

# component-Data Ingestion
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} download! with following inf: \n {headers}')
        
        else:
            logger.info(f"file already exists")


    def extract_zip_file(self):
        '''
        zip_file_path: str
        extracts the zip fole into the data data directory
        function retruns none
        '''
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)