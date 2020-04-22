#ch6_48 split()
'''str1 = "Silicon stone Education"
str2 = "D:\Python\ch6"
slist1 = str1.split()
slist2 = str2.split("\\")
print(str1, " 串列內容是 ", slist1)
print(str1, " 串列字數是 ", len(slist1))
print(str2, " 串列內容是 ", slist2)
print(str2, " 串列字數是 ", len(slist2))'''

#ch6_49 join()
'''path = ['D:', 'ch6', 'ch6_49.py']
connect = '\\'
print(connect.join(path))
connect = '*'
print(connect.join(path))'''

#ch6-7實作
'''mag = "FBI Mark told CIA Linda that the secret USB had given to FBI Peter"
times = mag.count("FBI")
print("FBI出現%d次" % times)
mag = mag.replace("FBI","XX")
print(mag)'''

#ch6-8實作
'''mag = input('請輸入字串，本程式會判斷是否為網址: ')
if mag.startswith("http://") or mag.startswith("https://") :
    print('你輸入的是網址')
else:
    print('你輸入的為無效網址')'''

#ch6-9實作
'''song = "Are you sleeping are you sleeping Brother John Brother John\
    Morning bells are ringing morning bells are ringing\
    Ding ding dong Ding ding dong"
song = song.split( )
print("歌詞字數為",len(song))
print(song)
wortimes = input("請輸入想查詢的字串: ")
print("此字串出現次數為: ", song.count(wortimes))'''
#ch6-10實作
people = ['Mary','Josh','Tracy']
print('目前邀請名單人員為: ', people,)
chooes = input('如果你想邀請其他人員請輸入"1",但你想刪除名單人員請輸入"2": ')
chooes = int(chooes)
if chooes == 1 :
    x = input('請輸入預想加入名單人員: ')
    if x not in people :
        people.append(x)
        print('已將你預邀請人員加入至名單!', people)
    elif x in people :
        print('你所輸入的人員已在名單內!')
elif chooes == 2 :
    y = input('請輸入預想刪除的人員: ')
    if y in people :
        people.remove(y)
        print('已將你所輸入人員刪除至名單!', people)
    elif y not in people :
        print('請確認你所輸入人員!名單輸入錯誤!')
