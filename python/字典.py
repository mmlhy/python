
achievement = {
    'stu1':66,
    'stu2':77,
    'stu3':99,
}
print(achievement['stu1'])
achievement['stu1'] = 80
print(achievement)
print(achievement.get('stu1'))
print('stu1' in achievement)
#delete
'''
del  achievement['stu1']
achievement.pop('stu2')
print(achievement)
'''
achievement.setdefault('stu4',[77,66,22])   #写入一个key与value
print(achievement['stu4'][0])
print(achievement.keys())   #all keys
print(achievement.values())     #all values

achievement1={
    'stu5':88,
    'stu9':66
}
achievement.update(achievement1)    #合并并且重复的更新
print(achievement.items())

c = achievement.fromkeys([6,7,8],"test")   #初始化  value 是引用 三个一样
print(c)


#多级字典

class_name = {
    "class1":{
        "wu":["mei","liang"],
        "li":["kai","pao"],
        "zhi":["yi","da",";i"]
    },
    "class2":{
        "zz":["sha","nai"],
        "xx":["asd","qqq"]
    }
}

class_name["class2"]["xx"][0] = 'qu'
print(class_name)

#通用循环方式

for i in achievement:
    print(i,achievement[i])

for k,v in achievement.items():
    print(k,v)