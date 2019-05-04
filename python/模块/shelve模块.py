import shelve

d = shelve.open('shelve_test')  # 打开一个文件
#print(d.get('test')) #获取
t = ["ss",'22']

name = ["alex", "rain", "test"]
d["test"] = name  # 持久化列表
d["t1"] = t  # 持久化类

d.close()