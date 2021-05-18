#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
print(1+1)
d = 1
print(type(d) )

# 数据容器
# 列表LIST = [true,2]
# 集合SET 不允许有重复值 = {'ee',3} 自动去重
# 字典DICT = {'year':2001} 键值对
list1 = [ 9,2,2,3,3,'aa','aa',True]
set1 = { 2,2,3,3,'aa','aa',True}
dict1 = {'year':2001}
print(set1)
print(list1[0])
print(dict1['year'])
dict1['a'] = 'rrrr'
print(dict1)

#条件判断语句 if  else
if  5>6 :
    print(1)
elif 5>5 :
    print(2)
else:
    print(3)

#循环语句 for while
sales = [123, 234, 456, 678, 901]
sumsales = 0

for sale in sales :
    sumsales += sale
print(sumsales)

#函数
lista = [1,2,3,4,5]
def get_sum(list):
    sum = 0
    for num in list :
        sum += num
    print(sum)
    return sum
get_sum(lista)

#average
print(np.average(lista))



#循环中止 break（一刀切）  continue(跳过)


'''
@Project : datasis
@File    : DAY01.py
@IDE     : PyCharm
@Author  : zhaoll
@Date    : 2021/5/10 11:55
'''
