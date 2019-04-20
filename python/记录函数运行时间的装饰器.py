#本质是函数

"""
原则1.不能修改被装饰函数的源代码
2.不能修改被装饰函数的调用函数
"""

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("the function run is %s"%(end_time-start_time))
    return warpper


@timmer
def test1(aaa):
    print(aaa)
    time.sleep(3)
    print("in the test1")

aaa = {"Asd":"Asd"}
test1(aaa)