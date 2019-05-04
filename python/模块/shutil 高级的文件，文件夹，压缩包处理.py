import shutil

#文件的copy
f1 = open('shutil原文本','r',encoding='utf-8')
f2 = open('shutilcopy文件','w',encoding='utf-8')

shutil.copyfileobj(f1,f2)
f1.close()
f2.close()

#文件的copy(不用打开文件)
shutil.copyfile('shutil原文本','shutilcopy文件')

#仅拷贝权限。内容、组、用户均不变

shutil.copymode('shutil原文本','shutilcopy文件')

#拷贝状态的信息，包括：mode bits, atime, mtime, flags

shutil.copystat('shutil原文本','shutilcopy文件')

#copy文件和权限
shutil.copy('shutil原文本','shutilcopy文件')

#拷贝文件和状态信息
shutil.copy2('shutil原文本','shutilcopy文件')

#copy目录
shutil.copytree('/home/miao/桌面/python/python/模块','/home/miao/桌面/python/python/模块1')

#delete目录
shutil.rmtree('/home/miao/桌面/python/python/模块1')

#move目录
shutil.move('/home/miao/桌面/python/词云','/home/miao/桌面/python/词云')

#创建压缩包并返回文件路径，例如：zip、tar
"""

    base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
    如：www                        =>保存至当前路径
    如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
    format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
    root_dir： 要压缩的文件夹路径（默认当前目录）
    owner： 用户，默认当前用户
    group： 组，默认当前组
    logger： 用于记录日志，通常是logging.Logger对象

"""
shutil.make_archive('/home/miao/桌面/python/python/模块','zip',root_dir='/home/miao/桌面/python/python/模块')

#zip压缩，解压
"""
import zipfile
# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()
"""
#tar压缩，解压
"""
import tarfile

# 压缩
tar = tarfile.open('your.tar','w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
tar.close()

# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()
"""




