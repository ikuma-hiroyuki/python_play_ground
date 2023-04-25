import yfinance as yf
import requests
import datetime

# LINE Notifyのトークンを設定
LINE_TOKEN = "ここにあなたのトークンを入力してください"

# 日経平均株価とダウ平均株価のシンボルを設定
NIKKEI_SYMBOL = "^N225"
DOW_SYMBOL = "^DJI"

# 前日の日付を取得
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# yfinanceを使用して前日の日経平均株価とダウ平均株価の終値を取得
nikkei_data = yf.Ticker(NIKKEI_SYMBOL).history(start=yesterday, end=today)
dow_data = yf.Ticker(DOW_SYMBOL).history(start=yesterday, end=today)

nikkei_close_price = nikkei_data['Close'][0]
dow_close_price = dow_data['Close'][0]

# LINEに通知するメッセージを作成
message = f"【前日の株価情報】\n日経平均株価：{nikkei_close_price}\nダウ平均株価：{dow_close_price}"

# LINE Notify APIを使用してメッセージを送信
line_notify_api = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': f'Bearer {LINE_TOKEN}'}
payload = {'message': message}
requests.post(line_notify_api, headers=headers, data=payload)
