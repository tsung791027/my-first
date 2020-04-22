print('請輸入數字 : ', end='  ')
ans=input()
while not ans.isdigit() :
    print('請輸入數字 : ', end='  ')
    ans=input()
print('你輸入的數字是 : ',ans )

fruits=['蘋果','香蕉']
for x in range(4) :
    print(f'{x:<3}*')
print('{:=^40s}'.format("傳說中的分隔線"))
print('{:-^40s}'.format('第三方程式庫random'))
import random
right = ['Right','Good','正確答案']
msg = random.choice(right)
print(msg)
print('{:=^40s}'.format("傳說中的分隔線"))
wrong = ['BB','答錯','wrong']
def words(sta=True):
    if sta :
        msg = random.choice(right)
    else :
        msg = random.choice(wrong)
    return msg
a = words(1==1)
print(a)
b = words(1<1)
print(b)
