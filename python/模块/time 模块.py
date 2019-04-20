import time
"""
三类
1.时间戳
2.格式化
3.元组 struct_time(turple)

"""


#时间戳

print(time.time())

#本地时间和时间世界的差距
print(time.timezone)
#是否使用夏令时
print(time.daylight)

#传入秒数返回元组类型

print(time.gmtime(1553432084.4165509))  #不传参默认UTC时间
x = time.gmtime(1553432084.4165509)
print(x.tm_hour)

#转化为当地时间
print(time.localtime(1553432084.4165509))


#元组型转化为时间戳
print(time.mktime(x))

#元组型转化为格式化型
print(time.strftime("%Y-%m-%d %H-%M-%S",x))
"""
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.

"""
#格式化转元组型
print(time.strptime("2019-03-24","%Y-%m-%d"))

#元组转化为固定格式的字符串型
print(time.asctime(x))

#时间戳转化为固定格式的字符串型
print(time.ctime(1553432084.4165509))



