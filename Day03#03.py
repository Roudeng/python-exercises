# 練習：試著用 Python 將網址當中的 domain 取出來。
# Requirements：
# 1. 讓使用者可以輸入一個網址
# 2. 利用程式取出網址當中的 domain 後輸出


s = input() # https://www.facebook.com/dscareer

url = s[8:].split('/') # 可和split寫在一起
url = url[0]
print(url) # www.facebook.com


