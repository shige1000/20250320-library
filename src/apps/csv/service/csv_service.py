import csv
from utils.singleton import Singleton
from apps.csv.service.csv_service_interface import CsvServiceInterface
from typing import List


class CsvService(Singleton, CsvServiceInterface):
    def __init__(self):
        # 初期化処理
        pass

    def create_csv(self, data: List[list], csv_path: str):
        """
        CSVファイルを作成するメソッド

        Args:
            data (List[list]): CSVファイルに書き込むデータ
            csv_path (str): 作成するCSVファイルのパス
        """
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def test(self):
        print("CSVService is working!")
