"""
all()  参数全为真
example
"""
print(all([1,2,3]))

"""
any() 参数任意为真
"""
print(any([0,0,0]))

"""
bin() 数字转化二进制
"""
print(bin(3))

"""
bool() 判断真假
"""
print(bool(1))

"""
bytes() 转化成字节格式
"""
print(bytes("asdas",encoding="utf-8"))

"""
callable()  是否可调用
"""
def asd(): pass
print(callable(asd))

"""
chr() 返回ascill码
"""
print(chr(98))

"""
ord() 返回ascill对应的数字
"""
print(ord('b'))

"""
exec() 将字符串变成可执行代码
"""
a = 'print("nihao")'
exec(a)

"""
complex() 复数
"""

"""
dir() 查看方法
"""
print(dir(dict))

"""
divmod() 除几次和余数
"""
print(divmod(5,2))
c = divmod(5,2)
print(c[0])

"""
eval() 字符串编译字典
"""

"""
filter()  根据函数过滤  多和匿名函数一起使用
"""
res = filter(lambda x:x<5,range(10))
# for i in res:
#     print(i)

"""
map() 对每个传进来的值 进行函数处理
"""

res = map(lambda x:x*x,range(10))
# for i in res:
#     print(i)

import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res)

"""
 frozenset()        不可变集合
"""
a = frozenset([1,2,3,4,5])

"""
globals() 返回程序所有变量
"""
print(globals())

"""
hash（） 找到哈西映射
"""
print(hash('c'))

"""
hex() 转化成16进制
"""
print(hex(123))

"""
locals（） 在函数中打印局部变量
"""

"""
oct() 转成八进制
"""

"""
round() 保留几位数
"""

print(round(3.1595,2))

"""
sorted()  排序
"""

"""
zip() 拼接
"""
a = [1,2,3]
b = ['a','b','c']

print(next(zip(a,b)))

"""
__import__() 如果引入包名为字符串这么用
"""
