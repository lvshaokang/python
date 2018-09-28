#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    项目名称：小象奶茶馆结算系统
    作者：Jiessie
    时间：2018-4-4
    版本：第三版（将购物过程、购物信息打印、购物详情记录各封装成函数，模块化代码，
        列表嵌套字典记录购物信息，每位顾客记录多个字典，根据消费口味划分
        字典记录会员信息（会员号和手机号）,
        增加每位顾客的购买品种，每位顾客每次可以多次输入（循环嵌套））
        增加顾客的购买品种数，将购物信息记录在字典中，模块化代码
"""


def shopping_procedure():
    goods_dic = {}
    milk_tea_no = input('请选择您要购买的奶茶编号：')
    while True:
        if milk_tea_no not in goods_dic.keys():
            if int(milk_tea_no) <= 5 and int(milk_tea_no) >= 1:
                milk_tea_amount = input('请输入您要购买的数量: ')
                goods_dic[milk_tea_no] = int(milk_tea_amount)
            else:
                print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')
        else:
            milk_tea_amount = input('请输入您要购买的数量: ')
            goods_dic[milk_tea_no] += int(milk_tea_amount)
        milk_tea_no = input('您还需要其它口味吗？请输入您要购买的奶茶编号，完成购物请选择Q：')

        if milk_tea_no.upper() == 'Q':
            break
    return goods_dic

    pass


def original_money(goods_dic):
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


def shopping_print(goods_dic):
    print('点单完成！您的购买详情为：')

    for milk_tea_no, milk_tea_amount in goods_dic.items():
        print('{}号奶茶:{}杯'.format(milk_tea_no, milk_tea_amount))

    total_money = original_money(goods_dic)
    print('您的总消费额为：{}元'.format(total_money))
    return total_money


def shopping_log(goods_dic, vip_no, total_consumer_record):
    for milk_tea_no, milk_tea_amount in goods_dic.items():
        single_consumer_record = {}
        single_consumer_record['vip_no'] = vip_no
        single_consumer_record['milk_tea_no'] = milk_tea_no
        single_consumer_record['milk_tea_amount'] = milk_tea_amount
        total_consumer_record.append(single_consumer_record)
    return total_consumer_record


def main():
    total_consumer_record = []
    vip_dic = {}
    i = 1
    total_money = 0

    while True:
        print('\n欢迎光临小象奶茶馆！小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！每次限尝鲜一种口味：\n 1）原味冰奶茶 3元  2）香蕉冰奶茶 5元 '
              ' 3) 草莓冰奶茶 5元  4）蒟蒻冰奶茶 7元  5）珍珠冰奶茶 7元')
        print('本店每日接待20位顾客，您是今天第{}位幸运儿'.format(i))

        goods_dic = shopping_procedure()
        vip_no = input('请输入您的专属会员号(新会员直接设置会员号即可，激活手机号方可享受会员价）：')
        total_money = shopping_print(goods_dic)

        if vip_no in vip_dic.keys():
            total_money *= 0.9
            total_money = round(total_money, 2)
            print('您可以享受会员价，折后总价：{}元'.format(total_money))
        else:  # 非会员则添加到会员表中
            vip_phone_no = input('请输入您的手机号激活会员: ')
            vip_dic[vip_no] = vip_phone_no

        total_consumer_record = shopping_log(goods_dic, vip_no, total_consumer_record)

        print("\n********************************************************")
        print('\t小象奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！诚挚欢迎您再次光临！')
        print("********************************************************")

        i += 1

        if i > 20:
            print('今日已闭店，欢迎您明天光临！')
            break


main()
