'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 10:14:29
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-14 10:29:51
FilePath: /Python-beginner/03章_变量/05_type_func.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
 
 #演示type函数的使用

name = 'tom' #字符串
age = 20   # 整型
score = 90.4 #浮点型（小数）
gender = "男" #字符串
is_pass = True #bool类型

#查看变量的类型（本质是查看变量指向的数据的类型）
print(type(name))
print(type(age))
print(type(score))
print(type(gender))
print(type(is_pass))
'''<class 'str'>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>'''

name = 100   #name指向数据类型发生变化时，type的结果也会改变
print(type(name))

#type可以直接查看具体的值（字面量）的类型
print(f"hello的类型是{type('hello')}")
print(f"1.1的类型是{type(1.1)}")
print(f"30的类型是{type(30)}")
print(f"True的类型是{type(True)}")

'''
hello的类型是<class 'str'>
1.1的类型是<class 'float'>
30的类型是<class 'int'>
True的类型是<class 'bool'>
'''