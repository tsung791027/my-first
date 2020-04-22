import os
path = r'C:\工作'
for dir_path , dir_names , file_names in os.walk(path) :
    print('目前路徑: ', dir_path)

    if len(dir_names) !=0:
        print('子目錄: ', dir_names)
    else:
        print('這裡面沒有子目錄')
    
    if len(file_names) !=0:
        print('檔案: ' , file_names)
    else:
        print('這裡沒有檔案')
    for f in file_names:
        print('檔案完整路徑: ', os.path.join(dir_path, f))


import shutil

total , used , free = shutil.disk_usage('.')
gb=2**30

print('磁碟容量: {:.2f} GB'.format(total / gb))
print('已使用容量: {:.2f} GB'.format(used / gb))
print('可使用容量: {:.2f} GB'.format(free / gb))

shutil.copy2('C:\工作\CR.JPG','C:\工作\影像')