# My Library

シンプルな計算機能を提供するPythonライブラリです。

## 機能

- 加算
- 減算
- 乗算
- 除算

## インストール

開発用インストール:
```bash
pip install -r requirements.txt
```

パッケージとしてインストール:
```bash
pip install -e .
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

## 使い方

```python
# 基本的な使い方
from my_library import add, subtract, multiply, divide

result_add = add(10, 5)        # 15
result_subtract = subtract(10, 5)  # 5
result_multiply = multiply(10, 5)  # 50
result_divide = divide(10, 5)    # 2.0
```
