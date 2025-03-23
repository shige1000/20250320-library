# 呼び出しのサンプル
import subprocess
import sys


def install_library():
    """
    Gitリポジトリからライブラリをインストールする
    """
    print("ライブラリをインストールしています...")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "git+https://github.com/shige1000/20250320-library.git"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        print("インストール完了")
        return True
    except subprocess.CalledProcessError as e:
        print(f"インストール失敗: {e}")
        return False


def main():
    """
    メイン処理
    """
    # ライブラリをインストール
    if not install_library():
        return

    # CSVサービスを利用するサンプル
    try:
        # クラスをインポート
        from apps.csv.service.csv_service import CsvService

        # インスタンス化
        csv_service = CsvService()

        # CSVファイル作成
        data = [
            ["名前", "年齢", "職業"],
            ["田中太郎", "28", "エンジニア"],
            ["山田花子", "32", "デザイナー"],
            ["佐藤一郎", "45", "マネージャー"]
        ]
        csv_service.create_csv(data, "output_data.csv")
        print("CSVファイルを作成しました: output_data.csv")

    except ImportError as e:
        print(f"インポートエラー: {e}")


if __name__ == "__main__":
    main()
