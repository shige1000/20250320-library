from abc import ABC, abstractmethod
from typing import List


class CsvServiceInterface(ABC):
    @abstractmethod
    async def create_csv(self, data: List[list], csv_path: str):
        pass
