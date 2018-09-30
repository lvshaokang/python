class WarehouseManageSys:
    def __init__(self):
        self.item_detail = {"老坛酸菜": 5, "红烧牛肉": 4, "酸辣粉": 6, "拉面": 7, "老干妈": 10, "乌江": 2, "王中王": 2, "蒜肠": 12, "淀粉肠": 8}

    def get_item_list(self, item_type):
        pm_list = ["老坛酸菜", "红烧牛肉", "酸辣粉", "拉面"]
        zc_list = ["老干妈", "乌江"]
        xc_list = ["王中王", "蒜肠", "淀粉肠"]

        if item_type == "pm":
            return pm_list
        elif item_type == "zc":
            return zc_list
        elif item_type == "xc":
            return xc_list
