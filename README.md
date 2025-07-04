# OpenCV combine movie
複数の動画ファイルを結合して一つの動画ファイルを書き出します。

## Environment / 環境

- Python 3.12.0
- opencv-python 4.11.0.86
- tqdm 4.66.2

パッケージ管理: `uv`

## Usage / 使い方

### モジュールのインストール

1. **初回インストール**（`pyproject.toml`／`uv.lock` から環境構築）  
   ```bash
   uv install
   ```

2. **差分同期**（既存環境との差分をインストール・アンインストール）  
   ```bash
   uv sync
   ```

3. **個別にインストール**（`uv` を使えない場合の例）
   ```
   pip install opencv-python tqdm
   ```

### 結合する動画ファイルの用意

結合したい動画ファイルを`media`ディレクトリに格納

## Sample usage / 実行方法

動画ファイルを結合

```
python combine.py
```

## Results / 出力結果

`output`ディレクトリに結合した動画ファイルが出力される。
