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

# 上の為替取得コードで取得できない場合は、以下のコードを使って取得してください。 (下の行の先頭の # を削除する)
# exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").history()["Close"].iloc[0]

# 両替を行う
result = args.amount * exchange_rate

# 結果を表示する
print(f"{args.amount} {args.from_currency} is equal to {result} {args.to_currency}")
