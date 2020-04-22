print('Ch2-1習題')
hourly_salary = 150  #設定時薪
annual_salary = hourly_salary * 8 * 300  #計算年薪
monthly_fee = 9000  #設定每月花費
annual_fee = monthly_fee * 12  #計算每年花費
annual_saving = annual_salary - annual_fee
print(annual_saving)
print('Ch2-2習題')
#單利率計算方式 利息 = 本金 * 利率 * 時間
interest = 50000 * 0.015 * 5
print('simple interesr = ',interest)
#假設本金為十萬 ，年利率為2%，複利計算10年後本金總合為
dubble_interest = 100000 *(1+0.02)**10
print('dubble interest = ',dubble_interest)
print('Ch2-4習題')
#一百顆蘋果分給23人 每天吃一顆 蘋果可以吃幾天，第幾天開始會不夠 多出幾顆
apples = 100
students = 23
day = apples // 23
apple = apples % 23
print('蘋果可以吃 = ',day,'天')
print('第',day+1,'天開始不足，並剩下',apple,'顆')
