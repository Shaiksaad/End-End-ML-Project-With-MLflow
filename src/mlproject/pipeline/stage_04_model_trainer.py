from mlproject.config.configuration import configration_manager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configration_manager()
        model_trainer_config  = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX===========X")
    except Exception as e:
        raise e