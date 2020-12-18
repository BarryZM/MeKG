import datetime

c_time = 'December 1,2018'
# c_time = 'Mar 09,2018'
c = 'May 2004'
ctime = datetime.datetime.strptime(c_time, "%B %d,%Y")
print(ctime)
ctime = datetime.datetime.strptime(c, "%B %Y")
print(ctime)
