#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    项目名称：小象奶茶馆结算系统
    作者：Jiessie
    时间：2018-3-31
    版本：第二版（更新了判断会员的方式，增加了每天服务顾客的数量并输出顾客次序,用列表记录会员号，嵌套列表记录每位会员的消费记录）
"""

total_consumer_record = []  # 定义记录所有消费者购物信息列表
vip_no_list = []  # 定义记录会员信息列表
i = 1  # 记录循环次数
while True:
    print('\n欢迎光临小象奶茶馆！小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！每次限尝鲜一种口味：\n 1）原味冰奶茶 3元  2）香蕉冰奶茶 5元 '
          ' 3) 草莓冰奶茶 5元  4）蒟蒻冰奶茶 7元  5）珍珠冰奶茶 7元')
    print('本店每日接待20位顾客，您是今天第{}位幸运儿'.format(i))
    ## 邀请顾客输入奶茶编号，并定义变量接收输入
    milk_tea_no = input('请选择您要购买的奶茶编号：')

    ## 根据输入的奶茶编号制定单价，使用判断语句
    if int(milk_tea_no) <= 5 and int(milk_tea_no) >= 1:

        ## 邀请顾客输入奶茶数量，并定义变量接收输入
        milk_tea_amount = int(input('请输入您要购买的数量: '))

        ## 根据输入的奶茶编号制定单价，使用判断语句
        if milk_tea_no == '1':
            price = 3
        elif milk_tea_no == '2' or milk_tea_no == '3':
            price = 5
        elif milk_tea_no == '4' or milk_tea_no == '5':
            price = 7

        ## 计算购物总价
        money = price * milk_tea_amount

        ## 输出购物信息
        print('您购买的是{}号奶茶，共购买{}杯，总计{}元'.format(milk_tea_no, milk_tea_amount, money))

        vip_no = input('请输入您的会员号(新会员直接设置会员号即可，第二次消费才可享受会员价）：')
        if vip_no in vip_no_list:  # 如果输入的会员号在会员信息列表中，则为老会员
            money *= 0.9
            money = round(money, 2)  # 会员价取两位小数
            print('您可以享受会员价，折后总价：{}元'.format(money))

        else:
            vip_no_list.append(vip_no)  # 如果输入的会员号不在会员信息列表中，那么为新会员，新会员信息记录在列表中

        # 记录每位顾客的消费列表
        single_consumer_record = []
        single_consumer_record.append(vip_no)
        single_consumer_record.append(milk_tea_no)
        single_consumer_record.append(milk_tea_amount)
        single_consumer_record.append(money)

        # 记录所有顾客消费列表
        total_consumer_record.append(single_consumer_record)

    else:
        print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')

    print("\n********************************************************")
    print('\t小象奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！诚挚欢迎您再次光临！')
    print("********************************************************")

    i += 1
    # 每天接待20位顾客，超过20位顾客时跳出循环
    if i > 20:
        print('今日已闭店，欢迎您明天光临！')
        break
