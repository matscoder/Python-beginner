'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 10:41:50
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-15 12:29:57
FilePath: /Python-beginner/03章_变量/16_homework02.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#使用str类型，分别保存 \n \t \r \\ 1 2 3 等字符，并打印输出
j = "\\n"
k = "\\t"
f = "\\r"
l = "\\\\"
m = "1"
n = "2"
p = "3"
print(f"{j} {k} {f} {l} {m} {n} {p}")

#正确写法：
str1 = '\n'
str2 = "\t"
str3 = "\r"
str4 = "\\"
str5 = "1"
str6 = "2"
str7 = "3"
print(str1, str2, str3, str4, str5, str6, str7,sep = "\t")