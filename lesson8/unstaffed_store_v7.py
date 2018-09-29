#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
无人便利店
功能：
	用户管理系统
	仓库管理系统
	货架管理系统
	升级购物车
'''
from lesson8.basic.warehouse import WarehouseManageSys
from lesson8.basic.rack import RackManageSys
from lesson8.basic.user import UserManageSys, BuyCar
from lesson8.basic.log import LogManageSys


class UntaffedStore:
    def shopping_hall(self):
        warehouse_manage = WarehouseManageSys()
        rack_manage = RackManageSys()
        user_manage = UserManageSys()
        log_manage = LogManageSys()

        pm_rack = []
        zc_rack = []
        xc_rack = []

        pm_rack_num = 1
        zc_rack_num = 1
        xc_rack_num = 1

        while True:
            print("*** 亲！欢迎光临无人便利店！***")
            user_id = ""
            while True:
                user_id = input("请输入手机号作为用户id使用：")
                if user_id != "":
                    if user_manage.user_id_check(user_id):
                        user_manage.add_new_user(user_id)
                        break
                    else:
                        print("请输入合法的手机号！")
                else:
                    print("手机号不能为空，请输入正确的手机号！")

            buy_car = BuyCar(user_id, user_manage)
            while True:
                rack_manage.check_add_rack(pm_rack, "pm", pm_rack_num, warehouse_manage)
                rack_manage.check_add_rack(zc_rack, "zc", zc_rack_num, warehouse_manage)
                rack_manage.check_add_rack(xc_rack, "xc", xc_rack_num, warehouse_manage)

                while True:
                    item_id = input("本店售卖商品：1泡面，2榨菜，3香肠。请输入想要购买的商品数字编号：")
                    if buy_car.item_id_check(item_id):
                        buy_car.add_item_2_car(pm_rack, zc_rack, xc_rack, item_id)
                        break
                    else:
                        print("请输入正确的商品编号！")

                if_buy = input("请输入y或者n选择是否继续购物:")
                if if_buy == "n":
                    if len(buy_car.car) > 0:
                        total_money = buy_car.account(warehouse_manage)
                        print("您的购物车商品如下：", buy_car.car)
                        print("购买的商品总价:{}".format(total_money))
                        log_manage.buy_log_manage(user_id, total_money, *buy_car.car)
                        print("欢迎下次光临")
                    else:
                        print("您没有购买任何商品！")
                    break


store = UntaffedStore()
store.shopping_hall()
