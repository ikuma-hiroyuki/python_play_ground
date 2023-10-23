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
exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").info['regularMarketPrice']

# 両替を行う
result = args.amount * exchange_rate

# 結果を表示する
print(f"{args.amount} {args.from_currency} is equal to {result} {args.to_currency}")

```

このプログラムをターミナルで実行するには、次のように入力します。

`python currency_converter.py USD JPY 1000`

この場合、1,000米ドルを日本円に両替します。

# 質問 ②:
```
Traceback (most recent call last):
  File "C:\Users\ikuma\PycharmProjects\python_play_ground\forex\forex.py", line 1, in <module>
    import yfinance as yf
ModuleNotFoundError: No module named 'yfinance'
```

# 回答 ②:

ModuleNotFoundError: No module named 'yfinance'というエラーは、yfinanceライブラリがインストールされていないことを意味しています。
yfinanceライブラリをインストールするには、次のようにコマンドを実行します。

`pip install yfinance`

また、Pythonのバージョンによっては、pipが正しく機能しないことがあります。その場合は、次のようにコマンドを実行して、pipをアップグレードできます。

`python -m pip install --upgrade pip`

これでyfinanceライブラリが正しくインストールされ、プログラムが正常に実行されるはずです。

# 質問 ③:

```
Traceback (most recent call last):
File "C:\Users\ikuma\PycharmProjects\python_for_beginner\forex\forex.py", line 12, in <module>
exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").info['regularMarketPrice']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
KeyError: 'regularMarketPrice'
```

というエラーになる

# 回答 ③:

ご指摘いただきありがとうございます。エラーが発生する原因は、Yahoo Finance APIがinfo属性にregularMarketPriceキーを提供しなくなったことです。
現在、代わりにregularMarketOpen、regularMarketDayHigh、regularMarketDayLow、regularMarketPreviousClose、
およびregularMarketPriceの代わりにregularMarketPriceの値が使用されます。つまり、以下のように修正する必要があります。

```pycon
import yfinance as yf
import argparse

# コマンドライン引数をパースする
parser = argparse.ArgumentParser(description='Currency converter')
parser.add_argument('from_currency', type=str, help='From currency symbol')
parser.add_argument('to_currency', type=str, help='To currency symbol')
parser.add_argument('amount', type=float, help='Amount to convert')
args = parser.parse_args()

# 為替レートを取得する
exchange_rate = yf.Ticker(f"{args.from_currency}{args.to_currency}=X").info['regularMarketOpen']

# 両替を行う
result = args.amount * exchange_rate

# 結果を表示する
print(f"{args.amount} {args.from_currency} is equal to {result} {args.to_currency}")
```

これでプログラムが正常に動作するはずです。また、取得したレートについて、正確にどの価格が使用されるかについては、yfinanceライブラリの更新状況によって変わる可能性があることに注意してください。

# 補足

次のレクチャー「米ヤフーファイナンスから昨日の日経平均株価とダウ平均株価を取得し LINE に通知する」で使っているyfinanceというライブラリのバージョンが撮影時点と変わりました。

そのため、配付資料と動画とで一部コードの記述が違う箇所があります。



正しく動作させるためには、動画内の以下のコードを

```
nikkei_close_price = nikkei_data['Close']
dow_close_price = dow_data['Close']
```

以下のコードに修正してください。

```
nikkei_close_price = nikkei_data['Close'].iloc[0]
dow_close_price = dow_data['Close'].iloc[0]
```



また、プログラムを実行するタイミング(株式市場が休日)でデータが取得できないためエラーになることがあります。その場合はタイミングをずらして実行してみてくださいませ。
