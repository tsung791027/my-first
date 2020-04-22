import time
now = time.localtime()
date_str = time.strftime('%Y/%m/%d',time.localtime())
print('現在日期: ',date_str)