# 質問 ①

ラインに一営業日前の日経平均株価とダウ平均株価の終値を通知するpythonスクリプトを生成してください

# 回答 ①

以下は、Pythonのyfinanceモジュールを使用して、前日の日経平均株価とダウ平均株価の終値を取得し、LINE Notify APIを使用してLINEに通知するスクリプトの例です。このスクリプトを実行するためには、yfinanceモジュールとrequestsモジュールをインストールする必要があります。

```python
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
```

このスクリプトを実行すると、LINEに以下のようなメッセージが送信されます。

```
【前日の株価情報】
日経平均株価：xxxxx
ダウ平均株価：xxxxx
```

注意: LINE Notify APIを使用するためには、まずLINE Notifyのアカウントを作成し、トークンを取得する必要があります。



# 補足

次のレクチャーで使っているyfinanceというライブラリのバージョンが撮影時点と変わりました。

そのため、配付資料と動画とで一部コードの記述が違う箇所があります。



正しく動作させるためには、動画内の以下のコードを

```
exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").info['regularMarketOpen']
```



以下に修正してください。

```
exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").history(period="1d")["Close"].iloc[0]
```



また、プログラムを実行するタイミング(株式市場が休日)でデータが取得できないためエラーになることがあります。その場合はタイミングをずらして実行してみてくださいませ。