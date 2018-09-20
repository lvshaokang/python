#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
日期和时间
'''
import time
import datetime

# 获取当前时间戳
# print(time.time())
# sleep(seconds) 程序睡眠等待时间，参数是秒
'''
start_time = time.time()
print("------------->")
time.sleep(2)
print("<-------------")
end_time = time.time()
print(end_time-start_time)
'''
# 获取到当前的日期和时间
# print(datetime.datetime.now())
# strftime日期时间格式化
# print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# 计算时间差值
'''
start_time = datetime.datetime.now()
time.sleep(5)
end_time = datetime.datetime.now()
print((end_time-start_time).seconds)
'''
# 时间戳转换成日期和时间
'''
ts = time.time()
print(ts)
print(datetime.datetime.fromtimestamp(ts))
print(datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d"))
'''
# 根据时间间隔获取指定的日期
'''
today = datetime.datetime.today()
print(today.strftime("%Y-%m-%d %H:%M:%S"))
timedelta = datetime.timedelta(days=1)
yesterday = today - timedelta
print(yesterday.strftime("%Y-%m-%d %H:%M:%S"))
'''
