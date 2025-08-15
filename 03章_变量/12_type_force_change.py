'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 09:20:07
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-15 09:27:58
FilePath: /Python-beginner/03章_变量/12_type_force_change.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#3. 如果需要对变量数据类型进行准还，只需要将数据类型作为函数名即可，这种方式就是显式转换/强制转转

#显式转换案例

i = 10
#使用了float函数，将i 变量的值转成了一个小数，并赋给了j
j = float(i)
print("j的类型", type(j), "j = ", j)   # j的类型 <class 'float'> j =  10.0
k = str(i)
print("k的类型", type(k), "k = ", k) # k的类型 <class 'str'> k =  10
print(k + 90)  #TypeError: can only concatenate str (not "int") to str  k形式已经变成了字符串


