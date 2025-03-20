# My Library

シンプルな計算機能を提供するPythonライブラリです。

## 機能

- 加算
- 減算
- 乗算
- 除算

## インストール

**重要**: テストを実行する前に必ずパッケージをインストールしてください。

1. 依存パッケージのインストール:
```bash
pip install -r requirements.txt
```

2. パッケージを開発モードでインストール (**必須**):
```bash
pip install -e .
```

このステップにより、モジュールのインポートパスが正しく設定され、テストが正常に実行できるようになります。

## テストの実行

ローカルでテストを実行するには：

```bash
pytest src/tests/
```

カバレッジレポートを含めるには：

```bash
pytest src/tests/ --cov=my_library
```

## GitHub Actions

このプロジェクトは、GitHub Actionsを使用して自動テストを実行します。プッシュやプルリクエストごとに、テストが自動的に実行されます。

ワークフローの設定は `.github/workflows/python-tests.yml` に定義されています。

### ブランチ保護ルール

このリポジトリでは以下のブランチ保護ルールを実装しています：

- `master`ブランチは`develop`ブランチからのプルリクエストでのみ更新可能
- `develop`ブランチは`feature/*`ブランチからのプルリクエストでのみ更新可能

## 使い方

```python
# 基本的な使い方
from apps.my_library import add, subtract, multiply, divide

result_add = add(10, 5)        # 15
result_subtract = subtract(10, 5)  # 5
result_multiply = multiply(10, 5)  # 50
result_divide = divide(10, 5)    # 2.0
```
