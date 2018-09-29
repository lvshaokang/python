#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


class UserManageSys:
    def __init__(self):
        self.user_id_set = set()

    def add_new_user(self, user_id):
        if user_id not in self.user_id_set:
            self.user_id_set.add(user_id)

    def if_vip(self, user_id):
        if user_id in self.user_id_set:
            return True
        else:
            return False

    def user_id_check(self, user_id):
        rs = re.match("1[3578]\d{9}$", user_id)
        if rs != None:
            return True
        else:
            return False


class BuyCar:
    def __init__(self, user_id, user_manage):
        self.user_id = user_id
        self.if_vip = user_manage.if_vip(user_id)
        self.car = []

    def add_item_2_car(self, pm_rack, zc_rack, xc_rack, item_id):
        if int(item_id) == 1:
            if len(pm_rack) >= 1:
                self.car.append(pm_rack[len(pm_rack) - 1])
                pm_rack.pop()
            else:
                print("亲！泡面卖完了！小二正在煮面。。。")
        elif int(item_id) == 2:
            if len(zc_rack) >= 1:
                self.car.append(zc_rack[len(zc_rack) - 1])
                zc_rack.pop()
            else:
                print("亲！榨菜卖完了！小二正在疯狂的切榨菜。。。")
        elif int(item_id) == 3:
            if len(xc_rack) >= 1:
                self.car.append(xc_rack[len(xc_rack) - 1])
                xc_rack.pop()
            else:
                print("亲！香肠卖完了！小二正在拼命的剁肉。。。")
        else:
            print("亲！您输入的商品还在火星，请输入在售的商品编号！")

    def account(self, warehouse_manage):
        total_money = 0
        for item in self.car:
            total_money += warehouse_manage.item_detail.get(item, 0)
        if self.if_vip:
            vip_money = total_money * 0.9
            total_money = float("%.2f" % vip_money)
        return total_money

    def item_id_check(self, item_id):
        if item_id != "":
            item_ids = ["1", "2", "3"]
            if item_id in item_ids:
                return True
            else:
                return False
        else:
            return False
