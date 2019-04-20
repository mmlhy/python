#每次循环生成一个元素
"""
a = (i*2 for i in range(10))

print(a.__next__())
for i in a:
    print(i)

"""

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b      #保持中断状态
        #print(b)
        a , b = b , a+b
        n = n + 1
    return 'done'  #异常打印的消息

# for i in fib(10):
#     print(i)

f = fib(3)
while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print(e.value)
        break