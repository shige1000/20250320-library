import csv
import asyncio
from utils import AsyncSingleton
from apps.csv.service.csv_service_interface import CsvServiceInterface
from typing import List


class CsvService(AsyncSingleton, CsvServiceInterface):
    # 非同期初期化が必要な場合はコメントを外して実装
    async def _async_initialize(self):
        print("CsvService 非同期初期化完了")

    async def create_csv(self, data: List[list], csv_path: str):
        """
        CSVファイルを作成するメソッド (非同期)

        Args:
            data (List[list]): CSVファイルに書き込むデータ
            csv_path (str): 作成するCSVファイルのパス
        """
        def _write_csv():
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)

        await asyncio.to_thread(_write_csv)
        print(f"CSVファイルが非同期で作成されました: {csv_path}")
