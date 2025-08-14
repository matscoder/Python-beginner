'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 13:44:53
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-14 14:08:56
FilePath: /Python-beginner/03章_变量/07_float_detail.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import sys


n1 = 4.5
n2 = -3.6
print("n1 = ", n1)
print("n2 = ", n2)

#浮点类型的表示形式
n3 = 5.12
n4 = .512  #0可以省略
print("n4 = ", n4)

#科学计数法形式：如： 5.12e2,   5.12E-2
n5 = 5.12e+2  #表示5.12乘10的2次方，前面的加号可以省略
print("n5 = ", n5)
n6 = 5.12E-2 #表示5.12除以10的2次方
print("n6 = ", n6)

#浮点数的最大和最小值
print(sys.float_info)


#浮点类型计算后，存在精度的损失，可以使用 Decimal 类进行精确计算
#老韩说如何解决
#1.为了避免浮点数的精度问题，可以使用Decimal 类进行精确计算
#2.如果使用Decimal 类，需要倒入Decimal 类

#导入Decimal 类
from decimal import Decimal

b = Decimal("8.1 ") / Decimal("3")
print("b = ", b)   # b = 2.7


b = 8.1 / 3   #正常值应该是2.7
print("b = ", b) # b =  2.6999999999999997   无限接近于7

