'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 15:05:17
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-20 10:23:07
FilePath: /Python-beginner/03章_变量/09_str_detail.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#讲解字符串使用注意事项


#使用引号（' 或 "） 包括起来，创建字符串
str1 = 'Tom说: “hello”'  #两个都是"" 会报错, 没有办法判断到什么时候结束
print(str1)  # "hello"
str2 = "jack说:'hi'"
print(str2) #'hi'

#查看数据类型
print(f"str2的类型:{type(str2)}")

#通过加号可以连接字符串, 拼接起来
print("hi" + "tom") # hitom

# Python 不支持单字符类型，单字符在Python 中也是作为一个字符串使用
str3 = "A"
print("str3类型", type(str3))  # str3类型 <class 'str'>


#用三个单引号 '''内容''', 或三个双引号"""内容"""可以使字符串内容保持原样输出
#在输出格式复杂的内容是比较有用的，比如输出一段代码
#如果前面有三个'''，里面就不能有''',不然会认为代码结束
content = '''be the cat's whiskers/pyjamas'''
print(content)

#加引号 → "content" 就变成了一个字符串字面量，代表字母 c-o-n-t-e-n-t，而不是之前存的值。
#不加引号 → content 会被当作变量使用，程序会去找这个变量里存的东西，然后打印出来。
#举个例子：
#content = '''be the cat's whiskers/pyjamas'''
#print(content)       # 输出变量里存的值 → be the cat's whiskers/pyjamas
#print("content")     # 输出字面量字符串 → content
#所以如果你想打印变量的值，就不能在它外面再加引号。


#在字符串前面加'r' 可以使整个字符串不会被转译
str4 = r"jack\ntom\tking" #jack\ntom\tking
print(str4)





#讲解字符串的驻留机制
str1 = "Hello"
str2 = "Hello"
str3 = "Hello"

# id()函数是, 可以返回对象/数据的内存地址
print("str1的地址:", id(str1))
print("str2的地址:", id(str2))
print("str3的地址:", id(str3)) 
#str1的地址: 4311079280
#str2的地址: 4311079280
#str3的地址: 4311079280  每次执行时候的值是不一样的

str1 = "abc123#"
str2 = "abc123#"
print(id(str1), id(str2))

num1 = -100
num2 = -100
print("----------")
print(id(num1), id(num2))


#sys中的intern方法可以强制2个字符串指向同一个对象 （强制s2和s1指向相同）
import sys

s1 = "abc#"
s2 = sys.intern(s1)  #让s2直接指向s1点数据空间，相当于强制使用同一个数据
print(s1)
print(s2)
print( s1 is s2)