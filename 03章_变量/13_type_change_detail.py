'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 09:31:24
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-28 10:22:31
FilePath: /Python-beginner/03章_变量/13_type_change_detail.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


#显式类型转换注意事项


#不管什么值的int, float都可以转成str, str(x) 将对象 x 转换为字符串
n1 = 100
n2 = 123.65
print(str(n1))
print(str(n2))


#int转成float时，会增加小数部分，比如123 - 123.0, 
# float转成int时，会去掉小数部分，比如 123.65 - 123

print(float(n1)) #100.0
print(int(n2))   #123


#str转int, float 使用 int(x), float(x) 将对象 x 转换为 int/float

n3 = "12.3" #字符串
#n4 = "123"
print(float(n3)) #12.3
print(int(n3))  #要从字符串转成整数，要求这个字符串本身就是一个整数————ValueError: invalid literal for int() with base 10: '12.3'
#print(int(n4))

#在将str类型转成基本数据类型时，要确保str值能够转成有效的数据，比如，可以把"123" 转成一个整数，但是不能把"hello"转成一个整数
#如果格式不正确，程序会报 ValueError, 程序就会终止
n4 = "hello"
print("float(n4)") 
print("int(n4)")


#5.对一个变量进行强制转换，会返回一个
i = 10
j = float(i)
print("i的值:", i, "i的类型:", type(i)) #10,int
print("j的值:", j, "j的类型:", type(j)) #10.0,float

k = str(i)
print("i的值:", i, "i的类型:", type(i)) #10,int
print("k的值:", k, "k的类型:", type(k)) #"10", str

