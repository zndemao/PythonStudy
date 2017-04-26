import os

print('返回当前的工作目录')
print(os.getcwd())
print('改变工作目录')
os.chdir('F:\\A')
print(os.getcwd())
print('列举指定目录中的文件名')
print(os.listdir())
print('创建单程层目录,如果该目录已经存在抛出异常')
os.mkdir("A")
print('递归创建多层目录,如果该目录已经存在抛出异常')
# os.makedirs()
print('删除文件')
os.remove()
print('删除单层目录，如果该目录非空则抛出异常')
os.rmdir()
print('递归删除目录，从子目录逐层尝试删除，遇到目录非空则抛出异常')
os.removedirs()
print('将文件old重命名为new')
os.rename()
print('运行系统的shell命令')
os.system()
'以下是支持路径操作中常用到打的一些定义，支持所有平台'
print('指代当前目录')
os.curdir  # 不是函数
print('指代上一级目录')
os.pardir
print('输出操作系统特定的路径分割符')
os.sep
print('当前平台所使用的行终止符')
os.linesep
print('指代当前使用的操作系统')
os.name
# 以下去网址
# http://bbs.fishc.com/forum.php?mod=viewthread&tid=45512&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403
