#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import time

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


#输出结果如下：
#2017-06-27 15:07:59
#Tue Jun 27 15:07:59 2017
#1459175064.0
