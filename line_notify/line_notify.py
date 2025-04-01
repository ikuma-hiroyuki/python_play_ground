import yfinance as yf
import datetime

# 日経平均株価とダウ平均株価のシンボルを設定
NIKKEI_SYMBOL = "^N225"
DOW_SYMBOL = "^DJI"

# 前日の日付を取得
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# 上の為替取得コードで取得できない場合は、以下のコードを使って取得してください。 (下の行の先頭の # を削除する)
# yesterday = today - datetime.timedelta(days=7)

# yfinanceを使用して前日の日経平均株価とダウ平均株価の終値を取得
nikkei_data = yf.Ticker(NIKKEI_SYMBOL).history(start=yesterday, end=today)
dow_data = yf.Ticker(DOW_SYMBOL).history(start=yesterday, end=today)

nikkei_close_price = nikkei_data['Close'].iloc[0]
dow_close_price = dow_data['Close'].iloc[0]

print('日経225', nikkei_close_price)
print('ダウ',dow_close_price)
