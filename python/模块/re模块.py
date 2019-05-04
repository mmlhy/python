"""
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
'[..]' 自定义匹配 ，小写字母  [a-z] ,字母[a-zA-Z]

'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}

"""

import re

re.match()   #从前往后搜索  找到一个停止
re.search()  #只要字符串里有就行  找到一个停止
re.findall()  #找到所有符合条件的 返回列表
re.split()  #按条件分割
re.sub(a,b,c) #把c中满足a的换乘b

flags模式

re.I #忽略大小写
re.S #.的时候也匹配\n