#ch7_30py
'''msg1 = "人機對話專欄,告訴我你的心聲吧,我會重複你告訴我的心事!"
msg2 = "輸入q可以結束程式"
msg = msg1 + '\n' + msg2 + '\n' + '= '
input_msg = ''
while input_msg !='q':
    input_msg = input(msg)
    if input_msg != 'q':
        print(input_msg)'''

#Ch7_32py
'''answer = 78
guess = 0
while guess != answer :
    guess = int(input('請輸入你要猜的數字 = '))
    if guess < answer :
        print('請猜數字大一點的˙')
    elif guess > answer :
        print('請猜數字小一點的')
    else :
        print('恭喜你答對了! 答案是%d' % answer)'''

#ch7_33py
'''n = int(input('請輸入一個數字 '))
sum = 0
while n != 0 :
    sum += n
    n = int(input('請輸入一個數字 '))
print('以上所加起來的總合是%d' % sum)'''

#ch7_35py
i = 1                       #初始設定
while i <= 9 :              #當i大於9跳出外層迴圈
    j = 1
    while j <= 9 :
        result = i * j
        print('%d*%d=%-3d' % (i, j, result), end=' ')
        j += 1
    print()
    i += 1