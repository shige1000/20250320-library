import csv
from utils.singleton import Singleton
from typing import List
from .csv_service_interface import CsvServiceInterface


class CsvService(Singleton, CsvServiceInterface):
    def create_csv(self, data: List[list], csv_path: str):
        """
        CSVファイルを作成するメソッド

        Args:
            data (List[list]): CSVファイルに書き込むデータ
            csv_path (str): 作成するCSVファイルのパス
        """
        with open(csv_path, "w") as f:
            writer = csv.writer(f)
            writer.writerows(data)
