'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 12:40:57
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-15 13:58:09
FilePath: /Python-beginner/03章_变量/18_homework04.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''




#4、编程实现如下效果 homework04.py
   #     姓名    年齢    成绩   性别     爱好
   #     XX      xX      xx      xx      xx

#要求：
#1）用变量将姓名、年龄、成绩、性别、爱好存储
#2）使用+
#3） 添加适当的注释
#4） 添加转义字符，使用一条语句输出

#定义需要的变量
name = "jack"
age = 20
score = 90.2
gender = "男"
hobby = "打篮球"
print("姓名\t年龄\t成绩\t性别\t爱好\n" + name
      + "\t" + str(age) + "\t" + str(score)
        + "\t" + gender + "\t" + hobby)
#按照规定的格式输出信息




a = "姓名"
b = "年龄"
c = "成绩"
d = "性别"
e = "爱好"

f = a + b + c + d + e#  中间再加" "当分隔符

g = "mats"
h = "20"
i = "90"
j = "男"
k = "摄影"

l = g + h + i + j + k

f = a + " " + b + " " + c + " " + d + " " + e  #chatgpt求助
l = g + " " + h + " " + i + " " + j + " " + k
print(f"{f}\n{l}")
