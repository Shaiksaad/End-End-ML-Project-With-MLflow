from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline


STAGE_NAME  = "Data Insgestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingesion = DataIngestionTraining_pipeline()
    data_ingesion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
except Exception as e:
        raise e

