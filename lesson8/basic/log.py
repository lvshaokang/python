#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import csv


class LogManageSys:
    def __init__(self):
        self.buy_logs = []

    def get_log_time(self, format):
        log_time = datetime.datetime.now().strftime(format)
        return log_time

    def write_log_append_csv(self, file_path, file_name, header, data):
        log_time = self.get_log_time("%Y%m%d")
        print("log_time:{}".format(log_time))
        new_file_name = file_path + file_name + "_" + log_time + ".csv"
        with open(new_file_name, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, header)
            writer.writerows(data)

    def buy_log_manage(self, user_id, money, *items):
        buy_log = {"user_id": user_id, "money": money, "items": items}
        self.buy_logs.append(buy_log)
        item_str = ""
        for item in items:
            if item_str == "":
                item_str = item
            else:
                item_str += "|" + item

        file_path = "d://"
        file_name = "user_buy_log"
        header = ["user_id", "money", "items"]
        buy_logs = [{"user_id": user_id, "money": money, "items": item_str}]

        self.write_log_append_csv(file_path, file_name, header, buy_logs)
