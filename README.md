# OpenCV combine movie
複数の動画ファイルを結合して一つの動画ファイルを書き出します。

## Environment / 環境

- Python 3.12.0
- opencv-python 4.11.0.86

パッケージ管理: `uv`

## Usage / 使い方

### モジュールのインストール

`1`の方法で直接`opencv-python`をインストールするか、uvで管理しているので`2`の方法でパッケージをインストールする。
   1. `pip install opencv-python`
   2. `uv add -r requirements.txt`

### 結合する動画ファイルの用意

結合したい動画ファイルを`media`ディレクトリに格納

## Sample usage / 実行方法

動画ファイルを結合

```
python combine.py
```

## Results / 出力結果

`output`ディレクトリに結合した動画ファイルが出力される。