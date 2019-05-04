import random

#生成随机浮点数  0<= n <1
print(random.random())
#生成随机浮点数  1<= n <3
print(random.uniform(1,3))

#随机整数 1<= n <=3
print(random.randint(1,3))
#随机整数 1<= n <3
print(random.randrange(1,3))

#传入序列在里面随机取一个值（列表，元组，字符串）
print(random.choice('asd'))
#传入序列在里面随机取两个值（列表，元组，字符串）返回列表
print(random.sample('asdaf',2))

"""
洗牌功能
"""
list = [1,2,3,4,5,6,7]
print(list)
random.shuffle(list)
print(list)
