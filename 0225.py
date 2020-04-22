print('輸入攝氏溫度: ', end = '  ')
c = input()
f = int(c)*(9/5)+32
print(f)

print('輸入房子坪數: ', end = '  ')
x = input()
s = int(x)*3.305
print('你的房子大約為%.1f平方公尺' % s)

print('輸入房子平方公尺數: ', end='  ')
p = input()
d = float(p)/3.305
print('你的房子大約為%.1f平方公尺' % d)