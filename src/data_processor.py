from titanic_data_loader import TitanicDataLoader
from config import ProcessConfig

class DataProcessor:
    def __init__(self,
                 process_config: ProcessConfig,
                 data_loader: TitanicDataLoader):
        self.config = process_config
        self.data_loader = data_loader
        self.processed_data = None

    def process_data(self) -> None:
        """
        Perform data processing
        :return:
        """

    def _fill_missing_values(self):
        """
        Fill missing values in columns
        :return:
        """

    def _normalize_values(self):
        """
        Find standard scores for continuous features
        :return:
        """

    def _categorify(self):
        """
        Assign numbers to categorical values
        :return:
        """
