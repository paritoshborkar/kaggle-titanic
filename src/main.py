from config import ModelDataPaths, ProcessConfig, ModelParams
from titanic_data_loader import TitanicDataLoader
from train import Trainer


def run_pipeline(paths: ModelDataPaths = ModelDataPaths(),
                 process_config: ProcessConfig = ProcessConfig(),
                 model_params: ModelParams = ModelParams()):
    """
    Runs data loading, data processing and training steps
    :return:
    """
    # Load data amd process data
    data = TitanicDataLoader(paths, process_config)
    # Train model with data, export model if expected
    model = Trainer(data=data,
                    params=model_params,
                    paths=paths)
    model.train()
    # Display results against validation
    model.display_metrics()


def make_prediction(paths: ModelDataPaths, test_input):
    """
    Make prediction with trained model
    :param paths:
    :param test_input:
    :return:
    """


if __name__ == '__main__':
    run_pipeline()
