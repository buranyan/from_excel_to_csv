# Excel to CSV Converter

このプログラムは `xlsx2csv` を使用して、Excel (`.xlsx`) の指定したシートを CSV に変換する Python スクリプトです。

## 📌 必要な環境

- Python 3.x
- `xlsx2csv` パッケージ

## 🔧 インストール

以下のコマンドを実行して `xlsx2csv` をインストールしてください：

```sh
pip install xlsx2csv
```

## 🚀 使い方

1. Python スクリプトを実行します。
2. 変換したい Excel ファイルの名前を入力します（例: `data.xlsx`）。
3. 変換したいシート名を入力します（例: `Sheet1`）。
4. 指定したシートが CSV ファイルとして出力されます。

### 実行例

```sh
python script.py
```

```
Excelファイル名を入力してください（例: data.xlsx）: data.xlsx
変換するシート名を入力してください（例: Sheet1）: Sheet1
✅ Sheet1 を data.csv に変換しました！
```

## ⚠ 注意点

- `.xlsx` 形式のみ対応（`.xls` には非対応）
- 指定したファイルが存在しない場合はエラーになります
- シート名を正しく入力してください

## 📜 ライセンス

このプロジェクトは MIT ライセンスの下で提供されています

