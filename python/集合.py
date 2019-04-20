
#无序的

list_1 = [2,4,6,8,10]
list_1 = set(list_1)

list_2 = set([1,3,5,4,6])
#list_2 = set([2,4,6,8,10,55])

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

#并集
print(list_1.union(list_2))
print(list_1 | list_2)

#差集  in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_1 - list_2)

#子集
print(list_1.issubset(list_2))   #是否子集
print(list_1 <=list_2)
print(list_1.issuperset(list_2))  #是否父集
print(list_1 >= list_2)

#对称差集
print(list_1.symmetric_difference(list_2))   #双方都没有（并集减交集）
print(list_1 ^ list_2)


print("--------------")
list_3 = set([55,66,99])
#是否存在交集
print(list_1.isdisjoint(list_3))

#增
list_1.add(99) #加一项
list_1.update([55,66,99]) #加多项
print(list_1)

#删

list_1.remove(99)
print(list_1)

t = list_1.pop()   #随机移除一个
print(t)

list_1.discard(66) #指定删除一个
print(list_1)