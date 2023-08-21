from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTraining_pipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTraining_pipeline
from mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME  = "Data Insgestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingesion = DataIngestionTraining_pipeline()
    data_ingesion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
except Exception as e:
        raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
except Exception as e:
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTraining_pipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
except Exception as e:
        raise e
    
    
STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
except Exception as e:
        raise e
    
