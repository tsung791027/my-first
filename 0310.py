#ch6_58py
'''accounts = []
account = input("請輸入新帳號 = ")
accounts.append(account)
print("深石公司系統")
ac = input("請輸入帳號 = ")
if ac in accounts:
    print("歡迎登入深石系統")
else :
    print("帳號輸入錯誤")'''

#ch6-12實作 
'''abc = "abcdefghijklmnopqrstuvwxyz"
fontabc = abc[:5]
end23 = abc[5:]
subtext = end23 + fontabc
print(subtext)'''

#ch7_3.py
'''players = ['Curry','Jordan','James','Durant','Obama']
for player in players :
    print(player)'''

#ch7-1實作
'''file1 = ['da1.jpg','da2.png','da3.gif','da4.gif','da5.jpg','da6.jpg','da7.gif']
Jpg = []
Png = []
Gif = []
for file3 in file1:
    if file3.endswith(".jpg"):
        Jpg.append(file3)
    elif file3.endswith(".png"):
        Png.append(file3)
    else :
        Gif.append(file3)
print(Jpg)
print(Png)
print(Gif)'''

#ch7-2實作
'''players = [['James',202],['Curry',193],['Durant',205],['Jordan',199],['David',211]]
high200 = []
for player in players:
    if player[1] > 200 :
        high200.append(player)
print(high200)'''

#ch7-3實作
'''x = 50
y = 1.2
for z in range(5):
    x = x+y
    print("%1f" % x)'''

##ch7-4實作
print("請輸入兩個數字,但數字2必須比數字1大")
n = int(input("請輸入數字1: "))
m = int(input("請輸入數字2: "))
if n > m :
    print("輸入錯誤!請確認數字是否在條件內!")
sum = 0
for num in range(n,m+1):
    sum += num
print("總和為 = ", sum)