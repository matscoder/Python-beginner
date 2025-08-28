'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 08:57:02
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-26 15:41:15
FilePath: /Python-beginner/03章_变量/11_type_change.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#隐式类型转换
# 1.python 根据该变量使用的上下文（即 当前值）在运行时决定的类型
var1 = 10
print(type(var1)) # int类型
var1 = 1.1
print(type(var1)) # float类型
var1 = "韩顺平教育"
print(type(var1)) #str类型


#2.在运算的时候，数据类型会向高精度自动转换，float的精度高于 int
var2 = 10
var3 = 1.2
var4 = var2 + var3
print("var4 = ", var4, "var4的类型:", type(var4)) # 11.2 float
var2 = var2 + 0.1
print("var2 = ", var2, "var2的类型:", type(var2)) # 10.1 float


#3. 如果需要对变量数据类型进行转换，只需要将数据类型作为函数名即可，这种方式就是显式转换/强制转换
