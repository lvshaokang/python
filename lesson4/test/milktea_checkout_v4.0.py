#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    项目名称：小象奶茶馆结算系统
    作者：Jiessie
    时间：2018-4-10
    版本：第四版（增加入店默认推荐，推荐其他顾客购买口味）
"""


# 定义购物过程函数
def shopping_procedure(vip_milkteano_list):
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

        if milk_tea_no.upper() == 'T':
            common_choose_list = []
            recomend_choose_list = []

            # 记录交集和差集
            for i in range(len(vip_milkteano_list)):
                common_choose = chosen_milk_tea_no & vip_milkteano_list[i]
                recommend_choose = vip_milkteano_list[i] - chosen_milk_tea_no
                if len(common_choose) != 0 and len(recommend_choose) != 0:
                    common_choose_list.append(common_choose)
                    recomend_choose_list.append(recommend_choose)

            if len(common_choose_list) == 0:
                if "4" not in chosen_milk_tea_no:
                    print('您可以尝尝我们的招牌4号蒟蒻冰奶茶！')
                else:
                    print('与您口味相同的其它顾客正在推荐的道路上……')

            else:
                # 记录交集元素长度
                len_common_choose_list = []
                for common in common_choose_list:
                    len_common_choose_list.append(len(common))

                rec_set = set()
                for len1, rec in zip(len_common_choose_list, recomend_choose_list):
                    if len1 == max(len_common_choose_list):
                        for rec1 in rec:
                            rec_set.add(rec1)

                # # 记录长度最大值索引值
                # rec_index = []
                # for i in range(len(len_common_choose_list)):
                #     if len_common_choose_list[i] == max(len_common_choose_list):
                #         rec_index.append(i)
                #
                # # 记录推荐元素集合
                # rec_set = set()
                # for index in rec_index:
                #     for rec in recommend_choose_list[index]:
                #         rec_set.add(rec)
                #
                print('买了以上口味的其他顾客还喜欢{}号奶茶'.format(max(rec_set)))

            milk_tea_no = input('您还需要其它口味吗？请选择您要购买的奶茶编号，完成购物请选择Q：')
            if milk_tea_no.upper() == 'Q':
                vip_milkteano_list.append(chosen_milk_tea_no)
                break

        elif milk_tea_no.upper() == 'Q':
            vip_milkteano_list.append(chosen_milk_tea_no)
            break

    return goods_dic


# 定义价格结算函数
def original_money(goods_dic):
    total_money = 0
    for milk_tea_no, milk_tea_amount in goods_dic.items():
        price = 0
        if milk_tea_no == '1':
            price = 3
        elif milk_tea_no == '2' or milk_tea_no == '3':
            price = 5
        elif milk_tea_no == '4' or milk_tea_no == '5':
            price = 7

        total_money += milk_tea_amount * price
    return total_money


# 定义购物信息打印函数
def shopping_print(goods_dic):
    print('点单完成！您的购买详情为：')

    for milk_tea_no, milk_tea_amount, in goods_dic.items():
        print('{}号奶茶:{}杯'.format(milk_tea_no, milk_tea_amount))

    total_money = original_money(goods_dic)
    print('您的总消费额为：{}元'.format(total_money))
    return total_money


# 定义记录所有顾客购物日志函数
def shopping_log(goods_dic, vip_no, total_consumer_record):
    for milk_tea_no, milk_tea_amount in goods_dic.items():
        single_consumer_record = {}
        single_consumer_record['vip_no'] = vip_no
        single_consumer_record['milk_tea_no'] = milk_tea_no
        single_consumer_record['milk_tea_amount'] = milk_tea_amount
        total_consumer_record.append(single_consumer_record)

    return total_consumer_record


# 主函数
def main():
    total_consumer_record = []
    vip_dic = {}
    vip_milkteano_list = []
    i = 1
    total_money = 0
    while True:
        print('\n欢迎光临小象奶茶馆！本店售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！\n 1）原味冰奶茶 3元  2）香蕉冰奶茶 5元 '
              ' 3) 草莓冰奶茶 5元  4）蒟蒻冰奶茶 7元  5）珍珠冰奶茶 7元')
        print('本店每日接待10位顾客，您是今天第{}位幸运儿'.format(i))

        goods_dic = shopping_procedure(vip_milkteano_list)
        vip_no = input('请输入您的专属会员号(新会员直接设置会员号即可，激活手机号方可享受会员价）：')
        total_money = shopping_print(goods_dic)

        if vip_no in vip_dic.keys():
            total_money *= 0.9
            total_money = round(total_money, 2)
            print('您可以享受会员价，折后总价：{}元'.format(total_money))
        else:  # 非会员则添加到会员表中
            vip_phone_no = input('请输入您的手机号激活会员：')
            vip_dic[vip_no] = vip_phone_no

        total_consumer_record = shopping_log(goods_dic, vip_no, total_consumer_record)

        print("\n********************************************************")
        print('\t小象奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！诚挚欢迎您再次光临！')
        print("********************************************************")

        i += 1

        if i > 10:
            print('今日已闭店，欢迎您明天光临！')
            break


main()
