"""
为了避免忘记关闭文件
可同时打开多个
"""

with open("yesterday",'r',encoding="utf-8") as f,open("yesterday2",'r',encoding="utf-8")as f1:
    for k in f1:
        print(k)