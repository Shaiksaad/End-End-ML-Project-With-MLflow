from mlproject.config.configuration import configration_manager
from mlproject.components.data_validation import DataValidation
from mlproject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configration_manager()
        data_validation_config  = config.get_data_validation_configuration()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
    except Exception as e:
        raise e