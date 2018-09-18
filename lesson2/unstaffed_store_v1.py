#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
无人便利店
功能：
    1.售卖商品：泡面、榨菜、香肠，不同商品摆放在不同的货架
    2.最后被放入货架的商品先被取走
    3.顾客输入不同的商品编号，在购物车中添加对应编号的商品
    4.当顾客输错商品编号，则跳出本次购物，再次让用户输入商品编号
    5.当所有的货架的商品都卖完后，提醒顾客，程序退出
    6.顾客在购物过程中可以随时结束购物
'''

# 定义货架
# 泡面货架
pm_rack = []
# 榨菜货架
zc_rack = []
# 香肠货架
xc_rack = []

# 方便面箱子
pm_list = ["老坛酸菜", "红烧牛肉", "酸辣粉", "拉面"]
# 榨菜箱子
zc_list = ["老干妈", "乌江"]
# 香肠箱子
xc_list = ["王中王", "蒜肠", "淀粉肠"]

# 向货架摆放商品
pm_rack_num = 2  # 设置货架的容量
while len(pm_rack) < pm_rack_num:
    # 根据货架商品数量与提供的商品数取余，获取添加到货架上的商品名称
    index = len(pm_rack) % len(pm_list)
    pm_rack.append(pm_list[index])

zc_rack_num = 1  # 设置货架的容量
while len(zc_rack) < zc_rack_num:
    # 根据货架商品数量与提供的商品数取余，获取添加到货架上的商品名称
    index = len(zc_rack) % len(zc_list)
    zc_rack.append(zc_list[index])

xc_rack_num = 1  # 设置货架的容量
while len(xc_rack) < xc_rack_num:
    # 根据货架商品数量与提供的商品数取余，获取添加到货架上的商品名称
    index = len(xc_rack) % len(xc_list)
    xc_rack.append(xc_list[index])

print("*** 亲！欢迎光临无人便利店！***")

buy_car = []

while True:
    if len(pm_rack) == 0 and len(zc_rack) == 0 and len(xc_list) == 0:
        print("--本店所有商品全部售罄--")
        break
    goods_num = input("本店售卖商品：1泡面，2榨菜，3香肠。请输入想要购买的商品数字编号：")
    if int(goods_num) == 1:  # 泡面
        if len(pm_rack) >= 1:
            buy_car.append(pm_rack[len(pm_rack) - 1])
            pm_rack.pop()
        else:
            print("亲！泡面卖完了！小二正在煮面。。。")
    elif int(goods_num) == 2:  # 榨菜
        if len(zc_rack) >= 1:
            buy_car.append(zc_rack[len(zc_rack) - 1])
            zc_rack.pop()
        else:
            print("亲！榨菜卖完了！小二正在疯狂的切榨菜。。。")
    elif int(goods_num) == 3:  # 香肠
        if len(xc_rack) >= 1:
            buy_car.append(xc_rack[len(xc_rack) - 1])
            xc_rack.pop()
        else:
            print("亲！香肠卖完了！小二正在拼命的剁肉。。。")
    else:
        print("亲！您输入的商品还在火星，请输入在售的商品编号！")
        continue

    if len(buy_car) > 0:
        print("您的购物车商品如下：", buy_car)
    else:
        print("您没有购买任何商品！")

    if_buy = input("请输入y或者n选择是否继续购物:")
    if if_buy == "n":  # n表示不再继续购物，程序退出
        break

print("欢迎下次光临，拜拜！")
