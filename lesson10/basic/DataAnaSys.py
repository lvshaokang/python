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
        new_user_dict = {}
        for data in datas:
            dt = data[1]
            rs = re.match("{}".format(ym), dt)
            if rs != None:
                user_num = new_user_dict.get(dt, 0) + 1
                new_user_dict[dt] = user_num
        m_new_user_count = 0
        for key, value in new_user_dict.items():
            m_new_user_count += value

        print("{}月每日新增用户数：{}".format(ym, new_user_dict))
        print("{}月累计新增用户数：{}".format(ym, m_new_user_count))

    def sale_report(self):
        ym = self.get_date(1, "%Y%m")
        file_dir = "d://buy_log//"
        files = self.log_manage.list_dir_file(file_dir)
        sale_money_dict = {}
        sale_count_dict = {}
        for file in files:
            if re.match("user_buy_log_{}".format(ym), file):
                file_path = file_dir + file
                datas = self.log_manage.read_log_csv(file_path)
                money = 0
                count = 0
                for data in datas:
                    money += float(data[1])
                    items = data[2].split["1"]
                    count += len(items)
                file_date = file[13:21]
                sale_money_dict[file_date] = money
                sale_count_dict[file_date] = count
        print("{}月每日销量：{}".format(ym, sale_count_dict))
        print("{}月每日销售额：{}".format(ym, sale_money_dict))

    def wechat_user_gender_report(self):
        itchat.login()
        friends = itchat.get_friends()
        male_count = 0
        female_count = 0
        other_count = 0
        for friend in friends[1:]:
            gender = friend["Sex"]
            if gender == 1:
                male_count += 1
            elif gender == 2:
                female_count += 1
            else:
                other_count += 1
        total = len(friends[1:])
        print("-------------------*微信好友分析报告*------------------")
        print("好友总数：{}".format(total))
        print("男性好友数：%d，占比：%.2f%%" % (male_count, float(male_count) / total * 100))
        print("女性好友数：%d，占比：%.2f%%" % (female_count, float(female_count) / total * 100))
        print("未知性别好友数：%d，占比：%.2f%%" % (other_count, float(other_count) / total * 100))
        datas = [male_count, female_count, other_count]
        labels = ["male", "female", "other"]
        self.get_pie(datas, labels)

    def wechat_user_location_report(self):
        itchat.login()
        friends = itchat.get_friends()
        province_dict = {}
        for friend in friends[1:]:
            province = friend["Province"]
            if province == "":
                province = "未知"
                province_dict[province] = province_dict.get(province, 0) + 1
            else:
                province_dict[province] = province_dict.get(province, 0) + 1
        print(province_dict)

    def get_pie(self, datas, labels):
        plt.rcParams["font.sans-serif"] = ["SimHei"]
        plt.figure(figsize=(8, 6), dpi=80)
        plt.axes(aspect=1)
        plt.pie(datas, labels=labels, autopct="%.2f%%")
        plt.title("微信好友性别分析图")
        plt.show()


das = DataAnaSys()
# das.wechat_user_gender_report()
das.wechat_user_location_report()
