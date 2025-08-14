'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 14:12:38
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-14 14:47:48
FilePath: /Python-beginner/03章_变量/08_bool_detail.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


#bool类型的基本使用
num1 = 100
num2 = 200
if num1 < num2:
    print("num1 < num2")

# 表示把 num1 > num2 的结果赋给 result变量
result = num1 > num2
print ("result = ", result)  #result输出了bool值 False

#看看result的数据类型
print("result的类型:", type(result))  #bool
print(type(1 > -1))  # 1 > -1是true, 是bool类型



#布尔类型可以和其他数据类型进行比较，比如数字，字符串等。
# 在比较时，Python会将Ture视为1，False视为0

b1 = False
b2 = True
print(b1 + 10) # 10
print(b2 + 10) # 11

#老师说明
# b1 = 0: 表示赋值，把0赋给b1
# b1 == 0: 表示判断 b1 是否和 0 相等
if b1 == 0:
    print("OK")

if b2 == 1:
    print("HI")

#在python中，非0被视为真值，0值被视为假值
#假值不会被输出，真值会被输出
if 0:
    print("哈哈")
if -1:
    print("嘻嘻")
if 1.1:
    print("嘻嘻")
if "老韩":   #把字符串当作bool（布尔）值来使用。非0值，会被输出
    print("老韩你好～")