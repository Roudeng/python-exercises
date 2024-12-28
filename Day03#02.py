# 練習：將字串當中的 not that poor 換成good。
# Requirements：
# 1. 輸入一個包含「not that poor 」的字串
# 2. 在程式中 not that poor 換成 good 後輸出

# s = input() # The company is not that poor!
# 法一
if s == 'The company is not that poor!':
  print('The company is good!')
else:
  print('wrong input!')

# 法二
output = s.replace('not that poor','good')
print(output)

print(s) # The company is good!
