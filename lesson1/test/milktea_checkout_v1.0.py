#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n欢迎光临小象奶茶馆！小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！每次限尝鲜一种口味：\n 1）原味冰奶茶 3元  2）香蕉冰奶茶 5元 '
      ' 3) 草莓冰奶茶 5元  4）蒟蒻冰奶茶 7元  5）珍珠冰奶茶 7元')
## 邀请顾客输入奶茶编号，并定义变量接收输入
milk_tea_no = input('请选择您要购买的奶茶编号：')

## 根据输入的奶茶编号制定单价，使用判断语句
if int(milk_tea_no) <= 5 and int(milk_tea_no) >= 1:

    ## 根据输入的奶茶编号制定单价，使用判断语句
    if milk_tea_no == '1':
        price = 3
    elif milk_tea_no == '2' or milk_tea_no == '3':
        price = 5
    elif milk_tea_no == '4' or milk_tea_no == '5':
        price = 7

    ## 邀请顾客输入奶茶数量，并定义变量接收输入
    milk_tea_amount = int(input('请输入您要购买的数量: '))

    ## 计算购物总价
    money = price * milk_tea_amount

    ## 输出购物信息
    print('您购买的是{}号奶茶，共购买{}杯，总计{}元'.format(milk_tea_no, milk_tea_amount, money))

    ## 输入是否为会员，并且定义变量接收输入
    if_vip = input('您是小象奶茶馆的会员吗(y/n)？')

    ## 判断是否为会员，会员享受9折优惠，并输出折后总价
    if if_vip == 'y':
        money *= 0.9
        print('您可以享受会员价，折后总价：{}元'.format(money))
else:
    print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')

print("\n********************************************************")
print('\t小象奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！诚挚欢迎您再次光临！')
print("********************************************************")
