from config import ModelDataPaths, ModelParams
from titanic_data_loader import TitanicDataLoader

from fastai.tabular.all import *
import pandas as pdw


class Trainer:
    """

    """

    def __init__(self,
                 data: TitanicDataLoader,
                 params: ModelParams = ModelParams(),
                 paths: ModelDataPaths = ModelDataPaths()):
        self.data = data
        self.params = params
        self.paths = paths
        self.model = self._create_model()

    def train(self):
        """
        Train model with provided model parameters
        :return:
        """

    def display_metrics(self) -> None:
        """
        Display metrics post training
        :return:
        """

    def _create_model(self) -> TabularLearner:
        """
        Returns a fastai TabularLearner object
        :return:
        """
        return tabular_learner()
