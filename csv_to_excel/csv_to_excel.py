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
