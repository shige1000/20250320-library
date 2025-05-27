from abc import ABC, abstractmethod
from typing import List


class BigqueryServiceInterface(ABC):
    @abstractmethod
    async def insert_data(self, data: List[dict], table_id: str):
        pass
