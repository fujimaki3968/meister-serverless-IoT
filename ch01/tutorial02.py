def hello(string):
    print('ハロー!', string)

# 奇数かどうかを判定する関数
def check_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

hello('サーバレスIoT')

num = 10
print("num:", str(num))

is_odd = check_odd(num)
# is_oddがTrueかどうか
if is_odd:
    print("これは奇数です")
else:
    print("これは奇数ではないです")