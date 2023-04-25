# 質問 ①

以下の形式のCSVファイルから平均年収500000以上の都道府県のみを抽出し、新規エクセルファイルに出力するpythonプログラムを生成してください。
ファイル名は`sample.csv`で、pythonプログラムと同じフォルダにあります。

CSVの形式
1列目:都道府県
2列目:県庁所在地
3列目:総人口
4列目:平均年収

出力は全列のタイトルと平均年収500万位滋養の都道府県を新規エクセルファイルに出力してください。

# 回答 ①

以下のようなコードで、CSVファイルから平均年収500万以上の都道府県のみを抽出し、新規エクセルファイルに出力できます。

```python
import csv
import openpyxl

# CSVファイルの読み込み
with open('sample.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 新しいエクセルファイルを作成
    wb = openpyxl.Workbook()
    ws = wb.active
    # タイトル行を追加
    ws.append(['都道府県', '県庁所在地', '総人口', '平均年収'])

    # 平均年収500万以上の都道府県のみを抽出して、エクセルファイルに追加
    for row in reader:
        if row[0] != '都道府県' and int(row[3]) >= 500000:
            ws.append(row)

    # エクセルファイルを保存
    wb.save('output.xlsx')
```

このコードを実行すると、`sample.csv`ファイルから平均年収500万以上の都道府県のみを抽出したデータが、新しいエクセルファイル`output.xlsx`に出力されます。

# 質問 ②

エクセルに出力される数値が文字列型になっているのでコードを修正してください。

# 回答 ②

CSVファイルから読み込んだ数値が文字列として扱われている場合は、以下のように修正することができます。 `int()`を使って文字列を整数に変換し、`value`
属性を使用してセルの値を上書きします。

```python
import csv
import openpyxl

# CSVファイルの読み込み
with open('sample.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 新しいエクセルファイルを作成
    wb = openpyxl.Workbook()
    ws = wb.active
    # タイトル行を追加
    ws.append(['都道府県', '県庁所在地', '総人口', '平均年収'])

    # 平均年収500万以上の都道府県のみを抽出して、エクセルファイルに追加
    for row in reader:
        if row[0] != '都道府県' and int(row[3]) >= 500000:
            # 数値を文字列型から数値型に変換
            row[2] = int(row[2])
            row[3] = int(row[3])
            ws.append(row)

    # エクセルファイルを保存
    wb.save('output.xlsx')
```

この修正により、エクセルファイルに出力される数値が数値型として扱われるようになります。

# 質問 ③

\>= 500000になっているので修正してください。

# 回答 ③

おっしゃる通りです。修正いたします。以下が修正後のコードとなります。

```python
import csv
import openpyxl

# CSVファイルの読み込み
with open('sample.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 新しいエクセルファイルを作成
    wb = openpyxl.Workbook()
    ws = wb.active
    # タイトル行を追加
    ws.append(['都道府県', '県庁所在地', '総人口', '平均年収'])

    # 平均年収500万以上の都道府県のみを抽出して、エクセルファイルに追加
    for row in reader:
        if row[0] != '都道府県' and int(row[3]) >= 5000000:
            # 数値を文字列型から数値型に変換
            row[2] = int(row[2])
            row[3] = int(row[3])
            ws.append(row)

    # エクセルファイルを保存
    wb.save('output.xlsx')
```

修正後は、平均年収の条件式が `>= 5000000` になります。