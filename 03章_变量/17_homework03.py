'''
Author: matscoder levin.hsu@outlook.com
Date: 2025-08-15 12:37:47
LastEditors: matscoder levin.hsu@outlook.com
LastEditTime: 2025-08-28 11:07:52
FilePath: /Python-beginner/03章_变量/17_homework03.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

#编程，保存两本书名，用+拼接，看效果。保存两本书价格，用+号拼接，看效果

i = "基督山伯爵"
j = "飘"
k = i + j
print(k)


#老韩答案
book1_name = "红楼梦"    
book1_price = 100.10
book2_name = "西游记"
book2_price = 200

print(book1_name + "\t" + book2_name)
print(book1_price + book2_price)