'''#ch6-5實作
scored = [87,60,99,34,77]
print(scored)
scored.sort(reverse=True)
print(scored)
scored.sort()
print(scored)
print(scored[-1])
print(sum(scored))'''
#ch6-34
'''James = [['Lebron James','SF','12/30/84'],23,19,22,31,18]
games = len(James)
print(games)
score_max = max(James[1:games])
i = James.index(score_max)
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名    : ", name)
print("位置    : ", position)
print("在第%d場得最高分%d" % (i,score_max))'''
#ch6-40
sc = [['宏璟揆',80,95,88,0,0],
['紅不浪',98,97,96,0,0],
['紅毛興',90,91,92,0,0],
['宏卯承',91,93,95,0,0],
['紅龍鴻',92,97,90,0,0]
]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
sc[2][4] = sum(sc[2][1:4])
sc[3][4] = sum(sc[3][1:4])
sc[4][4] = sum(sc[4][1:4])
print(sc[0])
print(sc[1])
print(sc[2])
print(sc[3])
print(sc[4])
test_time = len(sc[0][1:4])
print(test_time)
sc[0][5] = sc[0][4] / test_time
sc[1][5] = sc[1][4] / test_time
sc[2][5] = sc[2][4] / test_time
sc[3][5] = sc[3][4] / test_time
sc[4][5] = sc[4][4] / test_time
sc[0][5] = round(sc[0][5],1)
sc[1][5] = round(sc[1][5],1)
sc[2][5] = round(sc[2][5],1)
sc[3][5] = round(sc[3][5],1)
sc[4][5] = round(sc[4][5],1)
print(sc[0])
print(sc[1])
print(sc[2])
print(sc[3])
print(sc[4])

