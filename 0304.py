'''#ch6_8
jame = 23,19,22,31,18
print('最高得分: ',max(jame))
print('最低得分: ',min(jame))
print('得分總計: ',sum(jame))'''
'''#ch6_10
jame = 23,19,22,31,18
game = len(jame)
print('經過%d場比賽最高得分: '% game ,max(jame))
print('經過%d場比賽最低得分: '% game ,min(jame))
print('經過%d場比賽得分總計: '% game ,sum(jame))
'''
'''#ch6_19
car = ['Toyota','Nissan','Honda']
print('car串列長度是 = %d' % len(car))
if len(car) != 0 :
    del car[0]
    print('刪除cars串列元素成功')
    print('car串列長度是 = %d' % len(car))
else :
    print('car串列內沒有元素資料')
num = []
print('num串列長度是 = %d' % len(num))
if len(num) != 0 :
    del num[0]
    print('刪除num串列元素成功')
    print('num串列長度是 = %d' % len(num))
else :
    print('num串列內沒有元素資料')'''
'''#ch6_21
strN = ' DeepStone '
strL = strN.lstrip()
strR = strN.rstrip()
strB = strN.lstrip()
strB = strB.rstrip()
str0 = strN.strip()
print('/%s/' % strN)
print('/%s/' % strL)
print('/%s/' % strR)
print('/%s/' % strN)
print('/%s/' % str0)'''
'''#ch6-1實作
score = [87,99,69,52,78,98,80,93]
print('分數最高的是: ', max(score))
print('分數最低的是: ', min(score))
print('分數總合為: ', sum(score))'''
#ch6-2實作
'''banch = ['Toyota','Nissan','Honda']
print('舊的汽車銷售品牌:',banch)
banch[1] = 'Ford'
print('新的汽車銷售品牌: ', banch)'''
#ch6-3實作
'''str1 = '  Python '
str2 = 'is '
str3 = '  easy'
str1 = str1.lstrip()
str3 = str3.lstrip()
print(str1 + str2 + str3)'''
#ch6-4實作
citys = ['Taipe','Tokyo','Cebu','Seoul','Newyork']
print('五個城市為: ', citys)
citys.append('London')
print('增加為六個城市: ', citys)
citys.insert(3,'Xian')
print('將Xian插入: ', citys)
citys.remove('Tokyo')
print('將Tokyo刪除: ', citys)
