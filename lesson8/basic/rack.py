#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RackManageSys:
    def check_add_rack(self, rack, item_type, item_counts, warehouse_manage):
        if len(rack) == 0:
            print("正在更新货架，请稍等")
            while len(rack) < item_counts:
                item_list = warehouse_manage.get_item_list(item_type)
                index = len(rack) % len(item_list)
                rack.append(item_list[index])
