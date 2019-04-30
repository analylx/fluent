#-- Python模块搜索路径:
"""
(1)程序的主目录    (2)PYTHONPATH目录 (3)标准链接库目录 (4)任何.pth文件的内容
"""
#-- 查看全部的模块搜索路径
import sys
print(sys.path)
sys.argv                            # 获得脚本的参数
sys.builtin_module_names            # 查找内建模块
print(sys.platform)                        # 返回当前平台 出现如： "win32" "linux" "darwin"等
sys.modules                         # 查找已导入的模块
sys.modules.keys()
sys.stdout                          # stdout 和 stderr 都是类文件对象，但是它们都是只写的。它们都没有 read 方法，只有 write 方法
sys.stdout.write("hello")
sys.stderr
std_in = sys.stdin
