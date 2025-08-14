'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 09:35:23
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-14 10:06:25
FilePath: /Python-beginner/03章_变量/04_add_oper.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#程序中 + 号的使用

name = "king"
score = 50.8

print(score + 90) # 140.8

print(name + "hi") # king hi 字符串的拼接

print("100"+"98") #左右两边是字符串，里面有引号 #10098

print(34.5 + 100) #134.5


#代码，请分析输出结果
print(100 + 100)  #  200
print("100" + "100")  # 100100
print("100" + 3) #报错，python不允许一个数字和一个字符串相加，不知道想要干什么
# TypeError: can only concatenate str (not "int") to str



变量的类型由变量的值来决定