from mlproject.config.configuration import configration_manager
from mlproject.components.data_ingestion import DataIngestion
from mlproject import logger


STAGE_NAME  = "Data Insgestion Stage"

class DataIngestionTraining_pipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = configration_manager()
            data_ingestion_config  = config.get_data_ingestion_configuration()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.downlaod_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTraining_pipeline()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
    except Exception as e:
        raise e
    