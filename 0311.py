#ch7-6實作
'''fahrenheit = [32,77,104]
celsius = [(x-23)*5/9 for x in fahrenheit]
print(celsius)'''

#ch7-7實作
'''xlst = [n for n in range(2,21,2)]
print(xlst)'''

#ch7-8實作
'''xs = [1,2,3,4,5]
ys = [1,2,3,4,5]
z = [[x,y] for x in xs for y in ys]
for x,y in z:
    print(x,y)'''
#ch7_22py
'''for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print("aa",end="")
    print()'''

#ch7_24py
'''players =['Curry','Jordan','James','Durant','Obama','Kevin','Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)
index = 0
for player in players :
    if index == n:
        break
    print(player,end=" ")
    index += 1'''

#ch7-10實作
'''for i in range(1,10):
    for j in range(1,10):
        if j <= i :
            print(i,end="")
    print()'''

#ch7-13實作
'''xlst = [x for x in range(1,21)]
for y in xlst :
    if y == 2:
        print("%d是質數" % y)
    print()
else:
    for n in range(2,y):
        if y % n == 0 :
            print("%d不是質數" % y)
        print()
    else:
        print("%d是質數" % y)
    print()'''