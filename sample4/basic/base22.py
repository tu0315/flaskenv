import traceback

# try,exceptでキャッチする
try:
    # a = 10 / 0
    # b = ["10", "20", "30"]
    # a = b[4]
    c = b.method()
except ZeroDivisionError as e:
    # エラー詳細
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    traceback.print_exc()
# 全てのエラーをキャッチする
except Exception as e:
    print("Exception:", e, type(e))

print("処理が完了しました")
