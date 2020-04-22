'''a = [1,2,3,4,[5,6]]
b = a.copy()
a.append(8)
print(a,b)
a[4].append(7)
print(a,b)'''

'''fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
key = input('請輸入鍵 = ')
value = input('請輸入值 = ')
if key in fruits:
    print('%s已經存在字典了' % key)
else:
    fruits[key] = value
    print('新的fruits字典內容 = ', fruits)'''

#ch9_1實作
'''weeks = {'Monday':'星期一','Tuesday':'星期二','Wednesday':'星期三'
            ,'Thursday':'星期四','Friday':'星期五','Saturday':'星期六'
            ,'Sunday':'星期日'}
day = input('請輸入想要查詢的日子 = ')
day = day.title()
print(day)
if day in weeks:
    print(weeks[day])
else:
    print('請輸入錯誤資訊')'''
#ch9_2實作

'''months = {'January':'一月','February':'二月','March':'三月','April':'四月'
            ,'May':'五月','June':'六月','July':'七月','August':'八月','Setember':'九月'
            ,'October','十月','November':'十一月','December':'十二月'}'''

'''months = {'一月':'January','二月':'February','三月':'March','四月':'April'
            ,'五月':'May','六月':'June','七月':'July','八月':'August','九月':'Setember'
            ,'十月':'October','十一月':'November','十二月':'December'}
day = input('請輸入想要查詢的日子 = ')
if day in months :
    print(months[day])
else:
    print('請輸入錯誤資訊')'''

#ch9-18py
'''players = {'Stephen Curry':'Golden State Warriors',
            'Kevin Durant':'Golden State Warriors',
            'Lebron James':'Cleveland Cavaliers',
            'James Harden':'Houston Rockets',
            'Paul Gasol':'San Antonio Spurs'}
for name in players:
    print('姓名: ', name)'''

#ch9-21py
'''noodles = {'牛肉麵':'100','肉絲麵':'80','陽春麵':'60','大滷麵':'90','麻醬麵':'70'}
print(noodles)
noodlesLst = sorted(noodles.items(),key=lambda item: item[1])
print(noodlesLst)'''

#ch9_2實作
fruits = {'Watermelon':'15','Banana':'20','Pineapple':'25','Orange':'12','Apple':'18'}
print(fruits)
for fruit in sorted(fruits.items()):
    print(fruit)


noodles = {'牛肉麵':120,'肉絲麵':80,'陽春麵':60,'大滷麵':90,'麻醬麵':70}
print(noodles)
noodlesLst = sorted(noodles.items(),key=lambda item:item[1])
print(noodlesLst)
for x in noodlesLst:
    print(x)

print(noodles)
print(max(noodles.values()))
print(min(noodles.values()))
