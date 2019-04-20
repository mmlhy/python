
"""
打开文件的模式有：
    r，只读模式（默认）。
    w，只写模式。【不可读；不存在则创建；存在则删除内容；】
    a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件
    r+，可读写文件。【可读；可写；可追加】
    w+，写读
    a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
    rU
    r+U
"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

    rb
    wb
    ab

"""
#example1 直接打开
"""
#data = open("yesterday",encoding="utf-8").read()
f = open("yesterday",'r+',encoding="utf-8")  #文件句柄
data = f.read()
print(data)
f.write("\n我爱北京,\n天安门")
f.close()
"""

#example2 读前五行
"""
f = open("yesterday",'r+',encoding="utf-8")
for i in range(5):
     print(f.readline())   #读一行
f.close()
"""

#example3 整个文件 第十行输出----------
"""
f = open("yesterday",'r+',encoding="utf-8")
for index,line in enumerate(f.readlines()):  #小文件
    if index == 9:
        print("-------------")
        continue
    print(line)
f.close()
"""

#example4 大文件 读到内存一行 输出一行 在内存删除一行
"""
f = open("yesterday",'r+',encoding="utf-8")
for line in f:
    print(line)
f.close()
"""
#example5
"""
f = open("yesterday",'r+',encoding="utf-8")
print(f.tell()) #查看句柄位置
print(f.readline())
f.seek(0)  #改变句柄位置
print(f.readline())
print(f.encoding) #查看字符编码
print(f.name) #文件名子
print(f.readable())#是否可读
print(f.writable())#是否可写
f.close()
"""
#example6
"""
f = open("yesterday2",'w',encoding="utf-8")
f.write("hellow1\n")
f.write("hellow2\n")
f.flush() #强制把缓存区的内容刷到硬盘内
f.close()
"""
#example7
"""
import sys,time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
"""

#example8
"""
f = open("yesterday2",'a',encoding="utf-8")
f.truncate(10)  #如果不写数字 清空文件  写数字保留几个字符
f.close()
"""

#example9
f = open("yesterday2",'a',encoding="utf-8")

f.close()

