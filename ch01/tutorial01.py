# python 基本文法 tutorial

# print コンソールに出力
print("Hello, World!")

# titleという変数に文字列(string)を代入
title = "serverless IoT"
# title: str = "serverless IoT"  <- このように型を定義して代入も可能

# chapterという変数に整数(integer)を代入
chapter = 1
# chapter: int = 1

# chapter変数は文字ではないのでstr(変数)で文字列に変換
print(title + " chapter: " + str(chapter))

# input() で文字列の入力を取得
text = input("適当に文字を入力してください: ")

print("入力内容: " + text)

# len()で文字列の長さを取得
text_length = len(text)
print("文字列の長さ: " + str(text_length))

# if文 text_lengthが10だったら
if text_length == 10:
    print("この文字列は10文字です！")
# text_lengthが10ではなく、10より大きかったら
elif text_length > 10:
    print("この文字列の長さは10より大きいです")
# text_lengthが10でも10以上でもなかったら
else:
    print("この文字列の長さは10より小さいです")

print("-----------------------------")

print("1 + 1 = ", 1+1)
print("4 - 1 = ", 4-1)
print("2 x 2 = ", 2*2)
print("6 ÷ 3 = ", 6/3)

# わったあまりを求める
print("7を3で割ったあまり =", 7%3)

print("-----------------------------")

# 1から10を足す
sum_num = 0
for i in range(1, 11):
    sum_num += i
    print("sum_num +", i)

print("sum_num ->", sum_num)

print("-----------------------------")

# 配列(リスト)を作成　今回は文字列の配列
array = ['python', 'IoT', 'serverless', 'aws', 'cloud']

# arrayに入っている文字列の長さの合計を求める
sum_array_text_length = 0
for string in array:
    print("文字列: ", string)
    print("　長さ: ", str(len(string)))
    sum_array_text_length += len(string)

print("文字列合計:", sum_array_text_length)
