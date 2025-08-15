'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 08:44:41
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-15 08:47:50
FilePath: /Python-beginner/03章_变量/数据类型转换问题.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


n1 = 100
result = "n1的值是:" + n1
print(result)
#TypeError: can only concatenate str (not "int") to str
#两边都是字符串才能拼接, n1是int类型