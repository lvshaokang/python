'''
无人便利店
功能：
	1.将具有相同功能的代码封装成函数
	2.添加购物车结算功能
	3.货架商品卖完，自动补货
'''
#定义货架
#泡面货架
pm_rack = []
#榨菜货架
zc_rack = []
#香肠货架
xc_rack = []

#根据商品类型返回商品列表
def warehouse(item_type):
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

#检查货架并添加商品
def check_add_rack(rack,item_type,item_counts):
    if len(rack) == 0:
        print("正在更新货架，请稍等")
        while len(rack) < item_counts:
            # 根据货架商品数量与提供的商品数取余，获取添加到货架上的商品名称
            item_list = warehouse(item_type)
            index = len(rack) % len(item_list)
            rack.append(item_list[index])

#购物车结算
def buy_car_account(buy_car):
    #商品单价表
    item_detail = {"老坛酸菜":5, "红烧牛肉":4, "酸辣粉":6, "拉面":7,"老干妈":10, "乌江":2,"王中王":2, "蒜肠":12, "淀粉肠":8}
    total_money = 0
    for item in buy_car:
        total_money += item_detail.get(item,0)
    return total_money

#向货架摆放商品
pm_rack_num = 1 #设置货架的容量
zc_rack_num = 1 #设置货架的容量
xc_rack_num = 1 #设置货架的容量

print("*** 亲！欢迎光临无人便利店！***")
buy_car = []
while True:
    # 判断货架是否需要补货，自动补货
    check_add_rack(pm_rack, "pm", pm_rack_num)
    check_add_rack(zc_rack, "zc", zc_rack_num)
    check_add_rack(xc_rack, "xc", xc_rack_num)

    goods_num = input("本店售卖商品：1泡面，2榨菜，3香肠。请输入想要购买的商品数字编号：")

    if int(goods_num) == 1: #泡面
        if len(pm_rack) >= 1:
            break



