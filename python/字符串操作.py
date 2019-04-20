

name = "my \tname is miao {kkk}"
print(name.count('a'))  #查询字符个数
print(name.capitalize())#首字母大写
print(name.center(50,"-"))#补全字符并放中间
print(name.encode())#二进制
print(name.endswith("ao"))#什么结尾
print(name.expandtabs(tabsize=30))#修改\t空格数
print(name.find("name"))
print(name.format(kkk='aaaa'))#格式化
print(name.format_map({'kkk':'sds'}))#格式化
print(name.index('y'))#查位置
print(name.isalnum())#是否全为数字和字符
print(name.isalpha())#英文字符
print('1A'.isdecimal())#十进制
print(name.isdigit())#是否数字
print('sd'.isidentifier())#是否合法标识符
print(name.islower())#是否小写
print(name.isnumeric())#是否只是数字
print('ss'.isspace())#是否是空格
print('My Name Is'.istitle())#每个词的首字母是否都大写
print('My Name Is'.isprintable())#是否可打印
print(name.isupper())# 是否大写
print('+'.join(['1','2','3']))#用字符串连接join内的东西
print(name.ljust(50,'*'))#后面补字符
print(name.rjust(50,'='))#前面补字符
print('MIao'.lower())#小写
print('MIao'.upper())#大写
print('\n  MIao'.lstrip())#去左边的空格和回车
print('MIao\n  '.rstrip())#去右边的空格和回车
print('\n  MIao\n'.strip())#去空格和回车
p = str.maketrans('abcder','123456')#翻译列表
print('Miao'.translate(p))
print('Miao'.replace('a','d'))#替换
print('miao'.rfind('m'))#左向右查找返回最后一个下标
print('miao meng hah'.split()) #用split内的东西把字符串分成列表
print('Miao Meng hah'.swapcase())#大小写互换
print('miao meng hah'.title())#把每个词首字母大写
print(name.startswith('my'))#以什么开始
