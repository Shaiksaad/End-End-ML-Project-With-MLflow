from mlproject.config.configuration import configration_manager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path

STAGE_NAME  = "Data Transformation Stage"

class DataTransformationTraining_pipeline:
    def __init__(self) -> None:
        pass
    
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r")as f:
                status = f.read().split(" ")[-1]
                
            if status == "True":
                 config = configration_manager()
                 data_transformation_config  = config.get_data_transformation_configuration()
                 data_transformation = DataTransformation(config=data_transformation_config)
                 data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not valid!")
                
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTraining_pipeline()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
    except Exception as e:
        raise e

