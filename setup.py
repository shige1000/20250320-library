from setuptools import setup, find_packages


setup(
    name="20250320_library",
    version="0.1.0",
    description="よく利用する処理をまとめたライブラリ",
    author="shige1000",
    author_email="",
    url="git@github.com:shige1000/20250320_library.git",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        # ここに依存パッケージを追加
    ],
    classifiers=[
    ],
    python_requires=">=3.12",
)
