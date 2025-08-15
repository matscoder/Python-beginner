'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 10:13:36
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-15 10:31:39
FilePath: /Python-beginner/03章_变量/14_type_change_exercise.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

i = 10
j = float(i) # 10.0
print(type(i)) # int
print(type(j)) # float

i = j + 1 #11.0 -隐式转换
print(type(i))  #   float类型                          第一次思考错误，记成了浮点型不能和整型相加# 报错，数据类型不一致，j是浮点型，1是整型
print(type(j)) # float 类型

print(i) #  11.0   float类型
print(int(i))# 11
print(type(i))# float类型
 
# i指向11.0，int(i)产生了11，没有赋给任何变量，i没有任何变化，还是11.0，输出type(i),还是float类型，  这里很容易中招！  13行的题目