#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import datetime


class vipManagement:
    def __init__(self, vip_dic, today, total_cousumer_record):
        self.vip_no = input('请输入您的专属会员号(新会员直接设置会员号即可，激活手机号方可享受会员价）：')
        self.vip_dic = vip_dic
        self.today = today
        self.total_consumer_record = total_cousumer_record

    def if_vip(self, total_money):
        if self.vip_no in self.vip_dic.keys():
            total_money *= 0.9
            total_money = round(total_money, 2)
            print('您可以享受会员价，折后总价：{}元'.format(total_money))
        else:
            vip_dic = vipManagement.vip_dic_record(self)

    def vip_dic_record(self):
        vip_phone_no_str = input('请输入您的手机号激活会员：')
        vip_phone_no = vipManagement.if_phone_num_right(self, vip_phone_no_str)
        birthday = input('请输入您的生日（yyyymmdd):')
        sex = input('请输入您的性别（M/F):')
        constellation = input('请输入您的星座：')
        place = input('请输入您的所在地：')

        self.vip_dic[self.vip_no] = [vip_phone_no, birthday, sex, constellation, place, self.today]
        return self.vip_dic

    def if_phone_num_right(self, vip_phone_no):
        while True:
            if len(vip_phone_no) == 11:
                break
            else:
                vip_phone_no = input('对不起，您输入的手机号有误，请重新输入：')
        return vip_phone_no

    def write_csv_vip(self, day):
        f_vip_no = open('vip_no.csv', 'a', encoding='utf8')
        writer = csv.writer(f_vip_no)

        if day == 1:
            writer.writerow(['vip_no', 'phone_no', 'birthday', 'sex', 'constellation', 'place', 'enrolldate'])
        for key, values in self.vip_dic.items():
            if values[5] == self.today:
                values.insert(0, key)
                writer.writerow(values)
                del values[0]
        f_vip_no.close()


class Shopping:
    def __init__(self, vip_milkteano_list, total_consumer_record, today):
        self.vip_milkteano_list = vip_milkteano_list
        self.total_consumer_record = total_consumer_record
        self.today = today

    def shopping_procedure(self):
        goods_dic = {}
        buy_y_or_n = input('今日推荐招牌4号蒟蒻冰奶茶，是否购买（y/n)?')

        if buy_y_or_n.lower() == 'y':
            milk_tea_no = '4'
        elif buy_y_or_n.lower() == 'n':
            milk_tea_no = input('请选择您要购买的奶茶编号：')

        chosen_milk_tea_no = set()
        while True:
            if milk_tea_no not in goods_dic.keys():
                if int(milk_tea_no) <= 5 and int(milk_tea_no) >= 1:
                    milk_tea_amount = input('请输入您要购买的数量：')
                    goods_dic[milk_tea_no] = int(milk_tea_amount)
                    chosen_milk_tea_no.add(milk_tea_no)
                else:
                    print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')
            else:
                milk_tea_amount = input('请输入您要购买的数量：')
                goods_dic[milk_tea_no] += int(milk_tea_amount)

            milk_tea_no = input('您还需要其它口味吗？请输入您要购买的奶茶编号，选择T查看买了以上口味的其他顾客还喜欢什么口味，完成购物请选择Q：')

            if milk_tea_no.upper() != 'T' and milk_tea_no.upper() != 'Q':
                chosen_milk_tea_no.add(milk_tea_no)

            elif milk_tea_no.upper() == 'T':
                common_choose_list = []
                recommend_choose_list = []

                for i in range(len(self.vip_milkteano_list)):
                    common_choose = chosen_milk_tea_no & self.vip_milkteano_list[i]
                    recommend_choose = self.vip_milkteano_list[i] - chosen_milk_tea_no

                    if len(common_choose) != 0 and len(recommend_choose) != 0:
                        common_choose_list.append(common_choose)
                        recommend_choose_list.append(recommend_choose)

                if len(common_choose_list) == 0:
                    if '4' not in chosen_milk_tea_no:
                        print('您可以尝尝我们的招牌4号蒟蒻冰奶茶！')
                    else:
                        print('与您口味相同的其它顾客正在推荐的道路上……')
                else:
                    len_common_choose_list = []
                    for common in common_choose_list:
                        len_common_choose_list.append(len(common))

                    rec_index = []
                    for i in range(len(len_common_choose_list)):
                        if len_common_choose_list[i] == max(len_common_choose_list):
                            rec_index.append(i)

                    rec_set = set()
                    for index in rec_index:
                        for rec in recommend_choose_list[index]:
                            rec_set.add(rec)

                    print('买了以上口味的其他顾客还喜欢{}号奶茶'.format(max(rec_set)))

                milk_tea_no = input('您还需要其它口味吗？请选择您要购买的奶茶编号，完成购物请选择Q：')
                if milk_tea_no.upper() == 'Q':
                    self.vip_milkteano_list.append(chosen_milk_tea_no)
                    break

            elif milk_tea_no.upper() == 'Q':
                self.vip_milkteano_list.append(chosen_milk_tea_no)
                break
        return goods_dic

    def original_money(self, goods_dic):
        total_money = 0
        for milk_tea_no, milk_tea_amount in goods_dic.items():
            price = 0
            if milk_tea_no == "1":
                price = 3
            elif milk_tea_no == "2" or milk_tea_no == "3":
                price = 5
            elif milk_tea_no == "4" or milk_tea_no == "5":
                price = 7

            total_money += milk_tea_amount * price

        return total_money

    def shopping_print(self, goods_dic):
        print('点单完成！您的购买详情为：')

        for milk_tea_no, milk_tea_amount in goods_dic.items():
            print('{}号奶茶:{}杯'.format(milk_tea_no, milk_tea_amount))

        total_money = Shopping.original_money(self, goods_dic)
        print('您的总消费额为：{}元'.format(total_money))
        return total_money

    def shopping_log(self, goods_dic, vip_no):
        for milk_tea_no, milk_tea_amount in goods_dic.items():
            single_consumer_record = {}
            single_consumer_record['vip_no'] = vip_no
            single_consumer_record['milk_tea_no'] = milk_tea_no
            single_consumer_record['milk_tea_amount'] = milk_tea_amount
            single_consumer_record['date'] = self.today
            self.total_consumer_record.append(single_consumer_record)
        return self.total_consumer_record

    def write_csv_buy(self):
        f_record = open('user_buy_log_{}'.format(self.today), 'w', encoding='utf8')
        write2 = csv.writer(f_record)
        header = []
        for key in self.total_consumer_record[0].keys():
            header.append(key)

        write2.writerow(header)

        # i 为文件的行数
        for i in range(len(self.total_consumer_record)):
            data = []
            for z in self.total_consumer_record[i].values():
                data.append(z)
            write2.writerow(data)
        f_record.close()


if __name__ == '__main__':
    vip_dic = {}
    vip_milkteano_list = []
    day = 1

    while day <= 3:
        total_consumer_record = []
        today = datetime.date.today()

        today += datetime.timedelta(days=day - 1)

        print('\n今天是{},小象奶茶馆营业第{}天，美好的一天开始了！'.format(today, day))
        customer_no = 1

        while True:
            print('\n欢迎光临小象奶茶馆！本店售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！\n 1）原味冰奶茶 3元  2）香蕉冰奶茶 5元 '
                  ' 3) 草莓冰奶茶 5元  4）蒟蒻冰奶茶 7元  5）珍珠冰奶茶 7元')
            print('本店每日接待20位顾客，您是今天第{}位幸运儿'.format(customer_no))

            shopping = Shopping(vip_milkteano_list, total_consumer_record, today)
            goods_dic = shopping.shopping_procedure()
            vip_management = vipManagement(vip_dic, today, total_consumer_record)
            vip_no = vip_management.vip_no
            total_money = shopping.shopping_print(goods_dic)
            vip_management.if_vip(total_money)
            total_consumer_record = shopping.shopping_log(goods_dic, vip_no)

            print("\n********************************************************")
            print('\t小象奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！诚挚欢迎您再次光临！')
            print("********************************************************")

            customer_no += 1

            if customer_no > 2:
                print('今日已闭店，欢迎您明天光临！')
                break

        vip_management.write_csv_vip(day)

        shopping.write_csv_buy()

        day += 1
