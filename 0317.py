#ch8.1
'''numbers1 = (1,2,3,4,5)
fruits = ('apple','orange')
mixde = ('James', 50)
val_tuple = (10,)
print(numbers1)
print(fruits)
print(mixde)
print(val_tuple)
print(type(mixde))'''
#ch8_1
'''members = ('John', 'Peter', 'Curry', 'Mike', 'Kevin')
for member in members :
    print(member)'''

#ch8_2
'''members = ('John', 'Peter', 'Curry', 'Mike', 'Kevin')
members[0] = 'Johnnason'
print(members)'''

#ch8_3
'''members = ('John', 'Peter', 'Curry', 'Mike', 'Kevin')
print(members)
members = ('John', 'Peter', 'Curry', 'Mike', 'Kevin','Mary', 'Tom', 'Carlo')
print(members)'''

#ch8.10

'''keys = ('magic', 'xaab', 9099)
list_keys = list(keys)
list_keys.append('secret')
print(keys)
print(list_keys)'''

#ch8_4

'''tp = (1,2,3,4,5,2,3,1,4)
list_tp = list(tp)
list_tp.remove(2)
list_tp.remove(1)
list_tp.remove(3)
list_tp.remove(4)
newtp = tuple(list_tp)
print(newtp)'''

'''drinks = ['coffee', 'tea', 'wine']
enumberate_drinks = enumerate(drinks)
print(enumberate_drinks)
lit = list(enumberate_drinks)
print(lit)'''
#ch8_5

'''season = ('Spring', 'Summer', 'Fall', 'Winter')
chinese = ('春天', '夏天', '秋天', '冬天')
translater = list(zip(season,chinese))
print(translater)'''

#ch8.15
'''dist = 384400
speed = 1225
total_hours = dist // speed
data = divmod(total_hours, 24)
print("divmod 回傳的資料型態: ", type(data))
print("總共需要 %d 天" % data[0])
print("%d 小時" % data[1])
'''
#ch8_6
'''dayshightem = (30, 28, 29, 31, 33, 35 ,32)
dayslowtem = (20, 21, 19, 22, 23, 24, 20)
higher = max(dayshightem)
print(higher)
lower = min(dayslowtem)
print(lower)
avghigh = sum(dayshightem) / len(dayshightem)
avglow = sum(dayslowtem) / len(dayslowtem)
avg = (avghigh + avglow) / 2
print(avg)'''

#ch8_7

'''people = (1100, 652, 946, 821, 955, 1024, 1155)
avg = sum(people) / len(people)
print(avg)
var = 0
for v in people:
    var += ((v-avg)**2)
var = var / (len(people)-1)
print(var)'''

#ch9.9
'''fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print('舊的水果清單:', fruits)
objkey = '西瓜'
value = fruits.pop(objkey)
print('新的水果清單:', fruits)
print("刪除的水果", objkey, str(value))'''

