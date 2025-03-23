import csv
from utils.singleton import Singleton
from apps.csv.service.csv_service_interface import CsvServiceInterface
from typing import List


class CsvService(Singleton, CsvServiceInterface):
    def create_csv(self, data: List[list], csv_path: str):
        """
        CSVファイルを作成するメソッド

        Args:
            data (List[list]): CSVファイルに書き込むデータ
            csv_path (str): 作成するCSVファイルのパス
        """
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
