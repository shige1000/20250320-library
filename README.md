# My Library

シンプルな計算機能を提供するPythonライブラリです。

## 機能

- 加算
- 減算
- 乗算
- 除算

## インストール

```bash
pip install -r requirements.txt
```

## テストの実行

ローカルでテストを実行するには：

```bash
pytest tests/
```

カバレッジレポートを含めるには：

```bash
pytest tests/ --cov=my_library
```

## GitHub Actions

このプロジェクトは、GitHub Actionsを使用して自動テストを実行します。プッシュやプルリクエストごとに、テストが自動的に実行されます。

ワークフローの設定は `.github/workflows/python-tests.yml` に定義されています。
