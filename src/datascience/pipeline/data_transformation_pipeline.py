from pathlib import Path
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def iniate_data_transformation(self):
        try:
            with open(Path('artifacts\data_validation\status.txt')) as f:
                status = f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("You data scheme is invalid")
            
        except Exception as e:
            print(e)
                
            

