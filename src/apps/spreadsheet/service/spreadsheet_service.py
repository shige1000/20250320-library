from utils.singleton import Singleton
from googleapiclient.discovery import build, Resource
from google.oauth2.service_account import Credentials
from .spreadsheet_service_interface import SpreadsheetServiceInterface


class SpreadsheetService(Singleton, SpreadsheetServiceInterface):
    async def connect(self, credentials_path=None) -> Resource:
        """
        Google Sheets APIに接続するメソッド
        """
        if not credentials_path:
            raise ValueError("認証情報ファイルのパスが設定されていません")

        scope = [
            "https://www.googleapis.com/auth/spreadsheets",  # スプシの読み書き
            "https://www.googleapis.com/auth/drive",  # ドライブの読み書き
        ]

        try:
            credentials = Credentials.from_service_account_file(credentials_path, scopes=scope)
            client = build("sheets", "v4", credentials=credentials)
            return client
        except Exception as e:
            raise Exception(f"Google Sheets APIへの接続に失敗しました: {str(e)}")

    async def get_spreadsheet_object(self, client: Resource, spreadsheet_id: str) -> Resource:
        """
        Google Sheets APIのスプレッドシートオブジェクトを取得するメソッド
        """
        return client.spreadsheets().get(spreadsheetId=spreadsheet_id)
