from collections import Iterable,Iterator
"""
可用于for的是可迭代对象 Iterable
有next（）方法的是迭代器 Iterator
"""


print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

print(isinstance([],Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(range(10),Iterator))

#将可迭代对象变成迭代器

a = [1,2,3]
b = iter(a)
print(b.__next__())
print(next(b))