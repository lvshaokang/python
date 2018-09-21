'''
无人便利店
功能：
	用户管理系统
	仓库管理系统
	货架管理系统
	升级购物车
'''
import datetime
import csv


class WarehouseManageSys(object):
    def __init__(self):
        # 商品清单
        self.item_detail = {"老坛酸菜": 5, "红烧牛肉": 4, "酸辣粉": 6, "拉面": 7, "老干妈": 10, "乌江": 2, "王中王": 2, "蒜肠": 12, "淀粉肠": 8}

    # 根据商品类型返回商品列表
    def get_item_list(self, item_type):
        # 方便面箱子
        pm_list = ["老坛酸菜", "红烧牛肉", "酸辣粉", "拉面"]
        # 榨菜箱子
        zc_list = ["老干妈", "乌江"]
        # 香肠箱子
        xc_list = ["王中王", "蒜肠", "淀粉肠"]
        if item_type == "pm":
            return pm_list
        elif item_type == "zc":
            return zc_list
        elif item_type == "xc":
            return xc_list


# 货架管理系统
class RackManageSys(object):
    # 检查货架并添加商品
    def check_add_rack(self, rack, item_type, item_counts, warehouse_manage):
        if (len(rack)) == 0:
            print("正在更新货架，请稍等")
            while len(rack) < item_counts:
                # 根据货架商品数量与提供的商品数取余，获取添加到货架上的商品名称
                item_list = warehouse_manage.get_item_list(item_type)
                index = len(rack) % len(item_list)
                rack.append(item_list[index])
            print("当前货架货物有: {}".format(rack))


class UserManageSys(object):
    def __init__(self):
        # 存储用户信息，并对用户去重
        self.user_id_set = set()

    '''
    功能：添加新用户
    参数：
        user_id：用户编号
    '''

    def add_new_user(self, user_id):
        if user_id not in self.user_id_set:
            self.user_id_set.add(user_id)

    '''
    	功能：验证用户是否是VIP
    	参数：
    		user_id：用户编号
    	返回值：布尔类型
    '''

    def if_vip(self, user_id):
        if user_id in self.user_id_set:
            return True
        else:
            return False


'''
功能：日志管理
'''


class LogManageSys(object):
    def __init__(self):
        # 存储用户购买日志
        self.buy_logs = []
    '''
    功能：根据日志格式，返回当前格式化日期时间
    参数：
    	format：日期格式化方式，如：“%Y%m%d”
    '''
    def get_log_time(self,format):
        log_time = datetime.datetime.now().strftime(format)
        return log_time
    '''
    功能：将日志追加到csv日志文件进行持久化存储
    参数：
        file_path：文件路径
        file_name：文件名称
        header：文件标题
        data：日志数据:[{},{},...]
    '''
    def write_log_append_csv(self,file_path,file_name,header,data):
        log_time = self.get_log_time("%Y%m%d")
        print("log_time:{}".format(log_time))
        log_type = ".csv"
        new_file_name = file_path + file_name + "_" + log_time + log_type
        with open(new_file_name,"a",newline="",encoding="utf-8") as f:
            writer = csv.DictWriter(f,header)
            writer.writerows(data)

    '''
    功能：用户购买日志管理
    参数：user_id：用户编号（如：手机号）
    '''
    def buy_log_manage(self,user_id, money, *items):
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
        # 调用自身的方法
        self.write_log_append_csv(file_path,file_name,header,buy_logs)


class BuyCar(object):
    def __init__(self, user_id, user_manage):
        self.user_id = user_id
        self.if_vip = user_manage.if_vip(user_id)
        self.car = []

    '''
    功能：向购物车添加商品
    参数：
        pm_rack：泡面的货架
        zc_rack：榨菜的货架
        xc_rack：香肠的货架
        item_id：用户输入的商品编号
    '''

    def add_item2_car(self, pm_rack, zc_rack, xc_rack, item_id):
        if int(item_id) == 1:  # 泡面
            if len(pm_rack) >= 1:
                self.car.append(pm_rack[len(pm_rack) - 1])
                pm_rack.pop()
            else:
                print("亲！泡面卖完了！小二正在煮面。。。")
        elif int(item_id) == 2:  # 榨菜
            if len(zc_rack) >= 1:
                self.car.append(zc_rack[len(zc_rack) - 1])
                zc_rack.pop()
            else:
                print("亲！榨菜卖完了！小二正在疯狂的切榨菜。。。")
        elif int(item_id) == 3:  # 香肠
            if len(xc_rack) >= 1:
                self.car.append(xc_rack[len(xc_rack) - 1])
                xc_rack.pop()
            else:
                print("亲！香肠卖完了！小二正在拼命的剁肉。。。")
        else:
            print("亲！您输入的商品还在火星，请输入在售的商品编号！")

    '''
    功能：购物车自动结算
    参数：
        warehouse_manage:仓库管理系统对象
    '''

    def account(self, warehouse_manage):
        total_money = 0
        for item in self.car:
            total_money += warehouse_manage.item_detail.get(item, 0)
        if self.if_vip:
            vip_money = total_money * 0.9
            total_money = float("%.2f" % vip_money)
        return total_money


class UntaffedStore:
    # 购物大厅
    def shopping_hall(self):
        # 各种系统初始化
        warehouse_manage = WarehouseManageSys()
        rack_manage = RackManageSys()
        user_manage = UserManageSys()
        log_manage = LogManageSys()
        # 定义货架
        pm_rack = []  # 泡面货架
        zc_rack = []  # 榨菜货架
        xc_rack = []  # 香肠货架

        pm_rack_num = 3  # 设置货架的容量
        zc_rack_num = 2  # 设置货架的容量
        xc_rack_num = 1  # 设置货架的容量
        while True:
            print("*** 亲！欢迎光临无人便利店！***")
            user_id = ""
            while True:
                user_id = input("请输入手机号作为用户id使用：")
                if user_id != "":
                    user_manage.add_new_user(user_id)
                    break
                else:
                    print("手机号不能为空，请输入正确的手机号！")
            # 分配购物车
            buy_car = BuyCar(user_id, user_manage)
            while True:
                # 判断货架是否需要补货，自动补货
                rack_manage.check_add_rack(pm_rack, "pm", pm_rack_num, warehouse_manage)
                rack_manage.check_add_rack(zc_rack, "zc", zc_rack_num, warehouse_manage)
                rack_manage.check_add_rack(xc_rack, "xc", xc_rack_num, warehouse_manage)

                item_id = input("本店售卖商品：1泡面，2榨菜，3香肠。请输入想要购买的商品数字编号：")
                # 添加购物车
                buy_car.add_item2_car(pm_rack, zc_rack, xc_rack, item_id)
                if_buy = input("请输入y或者n选择是否继续购物:")
                if if_buy == "n":  # n表示不再继续购物，程序退出
                    if len(buy_car.car) > 0:
                        # 购物车结算
                        total_money = buy_car.account(warehouse_manage)
                        print("您的购物车商品如下：", buy_car.car)
                        print("购买的商品总价:{}".format(total_money))
                        # 用户购买日志
                        log_manage.buy_log_manage(user_id,total_money,*buy_car.car)
                        print("欢迎下次光临")
                    else:
                        print("您没有购买任何商品！")
                    break


store = UntaffedStore()
store.shopping_hall()
