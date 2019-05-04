import datetime

#现在的时间
print(datetime.datetime.now())

#三天前的时间  必须和now（）连用

print(datetime.datetime.now()+datetime.timedelta(-3))

#三天后
print(datetime.datetime.now()+datetime.timedelta(3))

#三小时前
print(datetime.datetime.now()+datetime.timedelta(hours=-3))

#时间的替换
c_time = datetime.datetime.now()
print(c_time.replace(hour=20,minute=33))