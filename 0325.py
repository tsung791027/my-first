#ch9-23py
'''armys = []
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
for soldier in armys[:4]:
    print(soldier)
print("小兵的數量 = ", len(armys))

#ch9-24py
for soldier in armys[35:38]:
    if soldier['tag'] == 'red' :
        soldier['tag'] = 'blue'
        soldier['score'] = 5 
        soldier['speed'] = 'medium'

print("列印編號35~40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

#ch9_6實作
for soldier in armys[47:50]:
    if soldier['tag'] == 'red' :
        soldier['tag'] = 'green'
        soldier['score'] = 10 
        soldier['speed'] = 'fast' 

print('列印最後五名小兵資料')
for soldier in armys[45:50]:
    print(soldier)'''

#ch9_7實作
'''wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                    'Kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
for account, account_info in wechat_account.items():
    print('使用者帳號 = ', account)
    name = account_info['last_name'] + ' ' + account_info['first_name']
    print('姓名 = ', name)
    print('城市 = ', account_info['city'])'''

#ch9-27
survey_dict = {}
market_survey = True

while market_survey:
    name = input('\n請輸入名字: ')
    travel_location = input('夢幻旅遊景點: ')

    survey_dict[name] = travel_location
    repeat = input('是否有人要參加市場調查?(N/Y): ')
    if repeat.title() != 'Y' :
        market_survey = False
print('\n\n以下是市場調查的結果') 
for user, location in survey_dict.items():
    print(user, '夢幻旅遊景點: ', location)