'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 10:38:23
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-14 13:44:24
FilePath: /Python-beginner/03章_变量/06_int_detail.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#讲解int类型的细节
# 在python中，int可以表示很大数
# the limit (4300 digits) for integer
#n3 = 9 ** 88  #9的88次方

n3 = 9 ** 888
print ("n3 = ", n3, type(n3))


#python的整数有10进制，16进制，8进制，2进制表示
print(10)
#十六进制
print(0x10)
#八进制
print(0o10)
#二进制
print(0b10)



#字节数随着数字增大而增大, 增量是4个字节
import sys  #你的代码报错是因为你用了 sys.getsizeof，但是没有导入 sys 模块。
            #Python 在使用标准库的模块时，必须先 import 才能用。

n1 =0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 30
n6 = 2 **128
#在python 中, 可以通过sys.getisizeof  查看返回对象(数据) 的大小 （按照字节单位返回）
#老师说明


print(n1, sys.getsizeof((n1)), "类型", type(n1))
print(n2, sys.getsizeof((n2)), "类型", type(n2))
print(n3, sys.getsizeof((n3)), "类型", type(n3))
print(n4, sys.getsizeof((n4)), "类型", type(n4))
print(n5, sys.getsizeof((n5)), "类型", type(n5))
print(n6, sys.getsizeof((n6)), "类型", type(n6))