#ch2-5.py 轉換成螢幕輸出
#momey = 50000*(1+0.015)**5
#print("本金合是")
#print(momey)
#ch2= open("ch2_5.txt", mode='w')
#print(momey, file=ch2)
#ch2.close
'''
d = 384400
x = 400
etom=d/x
print(etom)
ch25 = open("ch2_5.txt", mode='a')
print(int(etom), file=ch25)
ch25.close
'''
'''
#ch5_5
print('計算最終成績')
score = input("請輸入分數: ")
sc = int(score)
if (sc >= 90):
    print("A")
elif (sc >= 80):
    print("B")
elif (sc >= 70):
    print("C")
elif (sc >= 60):
    print("D")
else:
    print("F")
'''
#ch5_6
'''print("計算票價")
age = input("請輸入年紀: ")
age = int(age)
ticket = 100
if age >=80 or age <=6 :
    ticket = ticket*0.2
    print("票價是: %d" % ticket)
elif age >=60 or age <=12:
    ticket = ticket*0.5
    print("票價是: %d" % ticket)
else:
    print("票價是: %d" % ticket)'''
#ch5_7
'''print('判斷字元類別')
ch = input("請輸入字元: ")
if ord(ch) >= ord("A") and ord(ch) <=ord("Z"):
    print('這是大寫字元')
elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
    print('這是小寫字元')
elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
    print('這是數字字元')
else :
    print('這是特殊字元')'''
'''#ch5_9
height = input("請輸入身高(公尺): ")
weight = input("請輸入體寵(公斤): ")
bmi = int(weight)/(float(height)/100)**2
if bmi >= 18.5 and bmi <24.0 :
    print("BMI處於正常值")
else:
    print('BMI處於異常')'''
#Ch5_10
'''ans = 0
print("猜數字遊戲,請心中想一個0-7之間的數字,然後回答問題")
truefalse = "輸入y或Y代表有,其他代表無: "
q1 = "有沒有看到心中的數字 : \n" +\
     "1,3,5,7 \n"
num = input(q1 + truefalse)
print(num)
if num =="y" or num == "Y":
    ans +=1
truefalse = "輸入y或Y代表有,其他代表無: "
q2 = "有沒有看到心中的數字 : \n" +\
     "2,3,6,7 \n"
num = input(q2 + truefalse)
if num =="y" or num == "Y":
    ans +=2
truefalse = "輸入y或Y代表有,其他代表無: "
q3 = "有沒有看到心中的數字 : \n" +\
     "4,5,6,7 \n"
num = input(q3 + truefalse)
if num =="y" or num == "Y":
    ans +=4
print("讀者心中所想的數字是 : ", ans)'''
print("數字大小排列")
a = input("請輸入第一個數字: ")
b = input("請輸入第二個數字: ")
c = input("請輸入第三個數字: ")
if a > b and b > c:
    print(a,b,c)
elif a > b and b < c and a > c:
    print(a,c,b)
elif b > c and c > a :
    print(b,c,a)
elif b >c and c < a and b > a:
    print(b,a,c)
elif c > a and a > b :
    print(c,a,b)
else :
    print(c,b,a)