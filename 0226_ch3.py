a = 10
b = 18
c = 5
s = a+b-c
print(s)
s = 2*a+3-c
print(s)
s = b*c+20/b
print(s)
s = a%c*b+10
print(s)
s = a**c-a*b*c
print(s)
print('Ch2-2習題')
#單利率計算方式 利息 = 本金 * 利率 * 時間
interest = 50000 * 0.015 * 5
print(int(interest))
print(round(interest,1))
#月球離地球距離假設為384400KM，假設火箭飛行速度為250km/m ，請問到月球要幾分鐘
distance = 384400
speed_min = 250
speed_day = speed_min*60*24
day = distance/speed_day
print(int(day))
speed_hour = speed_min*60
hour = distance/speed_hour
print(int(hour))
min = distance/speed_min
print(int(min))
name ='李'
print(hex(ord(name)))
