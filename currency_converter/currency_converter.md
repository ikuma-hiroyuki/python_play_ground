# 質問 ①:

通過両替プログラムをpythonで生成してください。
ライブラリとして

- yfinance
- argparse
  を使ってください。

ターミナルの引数として

- 元通貨
- 両替後の通貨
- 通貨単位

を受け取るようにしてください。

# 回答 ①:

以下は、yfinanceおよびargparseライブラリを使用して、通貨の両替を行うPythonプログラムの例です。

```python
import yfinance as yf
import argparse

# コマンドライン引数をパースする
parser = argparse.ArgumentParser(description='Currency converter')
parser.add_argument('from_currency', type=str, help='From currency symbol')
parser.add_argument('to_currency', type=str, help='To currency symbol')
parser.add_argument('amount', type=float, help='Amount to convert')
args = parser.parse_args()

# 為替レートを取得する
exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").history(period="1d")["Close"].iloc[0]

# 両替を行う
result = args.amount * exchange_rate

# 結果を表示する
print(f"{args.amount} {args.from_currency} is equal to {result} {args.to_currency}")

```

このプログラムをターミナルで実行するには、次のように入力します。

`python currency_converter.py USD JPY 1000`

この場合、1,000米ドルを日本円に両替します。

# 補足

Macの場合コマンドを以下のようにします。

`python3 currency_converter.py USD JPY 1000`

<br>

プログラムを実行するタイミング(株式市場が休日)でデータが取得できないためエラーになることがあります。その場合はタイミングをずらして実行してみてくださいませ。
