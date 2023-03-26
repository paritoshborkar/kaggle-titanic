from config import ModelDataPaths, ProcessConfig

from fastai.tabular.all import DataLoaders
import pandas as pd


class TitanicDataLoader:
    def __init__(self, paths: ModelDataPaths = ModelDataPaths,
                 process_config: ProcessConfig = ProcessConfig()):
        self.paths = paths
        self.config = process_config
        self.data = self._process()

    def _process(self) -> DataLoaders:
        """
        Perform data processing and cleaning
        :return:
        """
        raw_data = self._load_data()

    def _load_data(self) -> DataLoaders:
        """
        Loads Data from using ModelDataPaths and returns a DataLoaders object
        :return:
        """