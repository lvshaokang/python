import datetime
import csv
from matplotlib import pyplot as plt


def read_user_buy_log(filepath, log_name):
    with open(filepath, "r") as f1:
        reader = csv.reader(f1)
        log_name = list(reader)
    return log_name


def data_transfer(log_name):
    new_log_name = []
    for i in range(len(log_name[0])):
        list = [log[i] for log in log_name]
        del list[0]
        new_log_name.append(list)
    return new_log_name


log_427 = 0
log_427 = read_user_buy_log('user_buy_log_2018-04-27', log_427)
new_log_427 = data_transfer(log_427)

log_428 = 0
log_428 = read_user_buy_log('user_buy_log_2018-04-28.csv', log_428)
new_log_428 = data_transfer(log_428)

log_429 = 0
log_429 = read_user_buy_log('user_buy_log_2018-04-29.csv', log_429)
new_log_429 = data_transfer(log_429)

log_430 = 0
log_430 = read_user_buy_log('user_buy_log_2018-04-30.csv', log_430)
new_log_430 = data_transfer(log_430)

log_501 = 0
log_501 = read_user_buy_log('user_buy_log_2018-05-01.csv', log_501)
new_log_501 = data_transfer(log_501)

vip_no = 0
vip_no = read_user_buy_log('vip_no.csv', vip_no)
new_vip_no = data_transfer(vip_no)


###########################################################################
# 输出每天新增vip人数列表，并画出折线图

def increased_vip(date, new_vip_no):
    increased_vip = []
    date_list = new_vip_no[-1]
    date = datetime.datetime.strftime(date, '%Y%m%d')
    for i in range(5):
        date1 = date + datetime.timedelta(days=1)
        date1 = datetime.date.isoformat(date1)
        increased_vip.append(date_list.count(date1))
        date1 = datetime.datetime.strftime(date1, '%Y-%m-%d')
        i += 1
    return increased_vip


increased_vip = increased_vip('20180427', new_vip_no)
print(increased_vip)

day = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5']
plt.plot(day, increased_vip, '-')
plt.title('Population of increased vip')
plt.show()

###########################################################################
# 绘制会员男女比例图

# 每个标签占多大，会自动去算百分比
sex = new_vip_no[4]
size_male = sex.count('M') + sex.count('m')
size_female = sex.count('F') + sex.count('f')
sizes = [size_male, size_female]

# 定义饼状图的标签，标签是列表
labels = ['Male', 'Female']
colors = ['red', 'yellow']

# 调节坐标轴刻度相同，使饼图为圆形
plt.axis('equal')

plt.pie(sizes, labels=labels, colors=colors, autopct='%2.lf%%')
plt.title('Gender composition of vip')
plt.show()


############################################################################
# 绘制每天各奶茶销售量柱形图
def create_consumption_dic(new_log):
    milktea_no = new_log[1]
    milktea_amount = new_log[2]
    consumption_dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}

    for i in range(len(milktea_amount)):
        for j in range(1, 6):
            if milktea_no[i] == str(j):
                consumption_dic[str(j)] += int(milktea_amount[i])
    return consumption_dic


def bar_plot(consumption_dic, date):
    plt.bar(consumption_dic.keys(), consumption_dic.values(), colors=('red', 'yellow', 'pink', 'green', 'blue'))
    plt.title('Bar plot for sales volume of milktea on {}'.format(date))
    plt.show()


consumption_dic_427 = create_consumption_dic(new_log_427)
consumption_dic_428 = create_consumption_dic(new_log_428)
consumption_dic_429 = create_consumption_dic(new_log_429)
consumption_dic_430 = create_consumption_dic(new_log_430)
consumption_dic_501 = create_consumption_dic(new_log_501)

bar_plot(consumption_dic_427, '2018-04-27')
bar_plot(consumption_dic_428, '2018-04-28')
bar_plot(consumption_dic_429, '2018-04-29')
bar_plot(consumption_dic_430, '2018-04-30')
bar_plot(consumption_dic_501, '2018-05-01')


############################################################################
# 绘制每种口味奶茶五天的销售量折线图

# num 奶茶种类

def create_eachmilktea_consumption(num):
    consumption_dic_427 = create_consumption_dic(new_log_427)
    consumption_dic_428 = create_consumption_dic(new_log_428)
    consumption_dic_429 = create_consumption_dic(new_log_429)
    consumption_dic_430 = create_consumption_dic(new_log_430)
    consumption_dic_501 = create_consumption_dic(new_log_501)

    eachmilktea_consumption = {
        'day1': consumption_dic_427[num],
        'day2': consumption_dic_428[num],
        'day3': consumption_dic_429[num],
        'day4': consumption_dic_430[num],
        'day5': consumption_dic_501[num],
    }
    return eachmilktea_consumption


def line_chart(eachmilktea_consumption, num):
    plt.plot(eachmilktea_consumption.keys(), eachmilktea_consumption.values(), '-', color="red", lineWidth=5)
    plt.title('Line chart for sales volumn of milktea {}'.format(num))
    plt.show()


milktea1_consumption = create_eachmilktea_consumption('1')
milktea2_consumption = create_eachmilktea_consumption('2')
milktea3_consumption = create_eachmilktea_consumption('3')
milktea4_consumption = create_eachmilktea_consumption('4')
milktea5_consumption = create_eachmilktea_consumption('5')

line_chart(milktea1_consumption, '1')
line_chart(milktea2_consumption, '2')
line_chart(milktea3_consumption, '3')
line_chart(milktea4_consumption, '4')
line_chart(milktea5_consumption, '5')
