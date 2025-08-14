'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-14 08:33:10
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-14 09:09:37
FilePath: /Python-beginner/03章_变量/03_format_output.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#格式化输出

#格式化输出案例
#定义变量
age = 80
score= 77.5
gender = '男'
name = "贾宝玉"

#  %操作符输出     前面的变量类型和后面的变量要匹配
print("个人信息: %s %d %s %.2f" %(name, age, gender, score))   #%.2f输出的值保留小数点两位，不够的加0 
#不匹配的情况
#print("个人信息: %d %d %s %.2f" %(name, age, gender, score))    #TypeError: %d format: a number is required, not str    str:字符串

#格式化输出在于中间可以任意空格，可以在不同答案之间自己指定格式
#例如空格，带个-等  *******

# format()函数 
print("个人信息: {} {} {} {}" .format(name, age, gender, score))

print("个人信息:  {} {} {}" .format(name, age, gender, score)) #前面三个占位符———— 不会报错

#print("个人信息:  {} {} {} {}" .format(name, age, gender)) #后面少一个对应的填充变量 ———— 会报错

#多可以，少填充变量不行




#f- strings    f是不能少的——————最方便的方法   [推荐]
print(f"个人信息:{name} {age} {score} {gender}")
#先定义再使用，不定义a无法输出
#print(f"个人信息:{name} {age} {score} {gender}{a}")