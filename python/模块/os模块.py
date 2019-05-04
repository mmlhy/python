import os

#获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())

#改变当前脚本工作目录；相当于shell下cd
os.chdir('/home/miao/桌面/python/python')
print(os.getcwd())

#返回当前目录: ('.')
print(os.curdir)

# 获取当前目录的父目录字符串名：('..')
print(os.pardir)

#可生成多层递归目录
os.makedirs('a/b/c')

#若目录为空，则删除，并递归到上一级目录，如上一层也为空，则删除，依此类推（清空文件夹）
os.removedirs('a/b/c')

#生成单级目录；相当于shell中mkdir dirname
os.mkdir('/home/miao/桌面/python/python/a')

#删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.rmdir('/home/miao/桌面/python/python/a')

#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.listdir('.'))

#删除一个文件
#os.remove()

#重命名文件/目录
#os.rename('oldname','newname')

# 获取文件/目录信息
print(os.stat(os.getcwd()))

# 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.sep)

#输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.linesep)

#输出用于分割文件路径的字符串
print(os.pathsep)

#输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.name)

#运行shell命令，直接显示
print(os.system("pwd"))

#获取系统环境变量
print(os.environ)

#返回path规范化的绝对路径
print(os.path.abspath(__file__))

#将path分割成目录和文件名二元组返回
print(os.path.split(__file__))

#返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname(__file__))

#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.basename(__file__))

#如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(__file__))

#如果path是绝对路径，返回True
print(os.path.isabs(__file__))

#如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile(os.path.dirname(__file__)))

#如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(os.path.dirname(__file__)))

#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join(os.path.dirname(__file__),os.path.basename(__file__)))

#返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime(__file__))

#返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime(__file__))