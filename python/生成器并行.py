import time
def consumer(name):
    print("%s 准备吃饱子了"%name)
    while True:
        baozi = yield

        print("包子 %s 来了，被%s 吃了"%(baozi,name))

# c = consumer("miao")
# c.__next__()
# b1 = "韭菜馅"
# c.send(b1)

def productor(name):
    c = consumer('A')
    c1 = consumer('B')
    c.__next__()
    c1.__next__()
    print("开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了两个包子")
        c.send(i)
        c1.send(i)

productor("miao")