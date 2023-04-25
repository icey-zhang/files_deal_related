import os
from re import L
logfile = open('/home/workshop/dataset/sen2/test.flist', 'r')
# loglist = logfile.readlines()
loglist = logfile.read().splitlines()
logfile.close()

#用txt文件确认文件夹
for line in loglist:        
    if os.path.exists(line.rstrip('\n')):
        print ("Found it")
    else:
        print ("Not Found!")
        logfile = open('test.txt', 'a+')
        logfile.write(str(line)+"\n")

for line in loglist:        
    new_line = line.rstrip('\n').replace('A','B').replace('s1_','s2_')
    if os.path.exists(new_line):
        print ("Found it")
    else:
        print ("Not Found!")
        logfile = open('test.txt', 'a+')
        logfile.write(str(new_line)+"\n")

#用文件夹确认txt文件
picdir = '/home/workshop/dataset/sen2/B/test/'
left1 = os.listdir(picdir)
# print(left1)
for x in left1:
    left_all = str(picdir).replace('B','A')+str(x).replace('B','A').replace('s2_','s1_')
    if left_all in loglist:
        print("check ok")
    else:
        print(x)
        logfile = open('test1.xt', 'a+')
        logfile.write(str(x)+"\n")
