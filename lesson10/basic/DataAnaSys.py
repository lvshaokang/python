from log import LogManageSys

import datetime
import re
import itchat
import matplotlib.pyplot as plt

'''
数据分析系统
	新增用户日报表
	销售日报表
'''


class DataAnaSys:
    def __init__(self):
        self.log_manage = LogManageSys()

    def get_date(self, days, format):
        today = datetime.datetime.today()
        timedelta = datetime.timedelta(days=days)
        target_date = today - timedelta
        return target_date.strftime(format)

    def user_report(self):
        ym = self.get_date(1, "%Y%m")
        datas = self.log_manage.read_log_csv("d://user_info.csv")
