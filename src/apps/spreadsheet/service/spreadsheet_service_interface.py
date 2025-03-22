from abc import ABC, abstractmethod
from googleapiclient.discovery import Resource


class SpreadsheetServiceInterface(ABC):
    @abstractmethod
    async def connect(self, credentials_path: str) -> Resource:
        pass

    @abstractmethod
    async def get_spreadsheet_object(self, client: Resource, spreadsheet_id: str) -> Resource:
        pass
