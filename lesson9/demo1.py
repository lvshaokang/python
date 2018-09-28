'''
排序算法
'''
# 冒泡排序
'''
len(list) = n
轮数：n-1
每轮两两元素比较的次数：n - i - 1 (i:已经排好序的元素个数，等于已经排序过的轮数)
'''
'''
参数：data_list:待排序的元素列表
'''


def bubble_sort(data_list):
    num = len(data_list)  # 待排序元素个数
    for i in range(0, num - 1):  # 控制总轮数
        for j in range(0, num - i - 1):  # 控制每轮循环两个元素互相比较的次数
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]


'''
选择排序
待排序元素有n个，共需要进行n-1轮排序
'''


# data_list待排序列表
def select_sort(data_list):
    list_len = len(data_list)
    for i in range(0, list_len - 1):  # 控制排序轮数
        tmp_min_index = i  # 初始假设最小值脚标
        for j in range(i + 1, list_len):
            if data_list[tmp_min_index] > data_list[j]:
                tmp_min_index = j  # 更新临时最小值脚标
        if i != tmp_min_index:  # 如果初始假设最小值脚标与临时最小值脚标不等，则交换两个元素的位置
            data_list[i], data_list[tmp_min_index] = data_list[tmp_min_index], data_list[i]


'''
快速排序
基准值：默认待排序的第一个元素
使用临时变量存储基准值
高位游标，和低位游标，
'''


def quick_sort(data_list, start, end):
    # 递归结束标识
    if start >= end:
        return
    # 低位游标
    low_index = start
    # 高位游标
    high_index = end
    # 基准值
    basic_data = data_list[start]
    while low_index < high_index:
        # 如果高位游标指向的元素>=基准值，高位游标向左移动一位
        while low_index < high_index and data_list[high_index] >= basic_data:
            high_index -= 1

        if low_index != high_index:
            # 当高位游标指向的元素小于基准值，则移动到该值到低位游标指向的位置
            data_list[low_index] = data_list[high_index]
            low_index += 1  # 低位游标向右移动一位

        ##如果低位游标指向的元素<基准值，低位游标向右移动一位
        while low_index < high_index and data_list[low_index] < basic_data:
            low_index += 1

        if low_index != high_index:
            # 当低位游标指向的元素大于等于基准值，则移动到该值到高位游标指向的位置
            data_list[high_index] = data_list[low_index]
            high_index -= 1  # 高位游标向左移动一位
    # 基准值所在位置
    data_list[low_index] = basic_data
    quick_sort(data_list, start, low_index - 1)  # 对基准值左侧未排序元素采用快速排序
    quick_sort(data_list, high_index + 1, end)  # 对基准值右侧侧未排序元素采用快速排序


'''
归并排序
'''


def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    # 根据列表长度确定拆分的中间位置
    mid_index = len(data_list) // 2
    # left_list = data_list[:mid_index]
    # right_list = data_list[mid_index:]
    left_list = merge_sort(data_list[:mid_index])
    right_list = merge_sort(data_list[mid_index:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    l_index = 0  # 左侧列表游标
    r_index = 0  # 右侧列表游标
    merge_list = []
    while l_index < len(left_list) and r_index < len(right_list):
        if left_list[l_index] < right_list[r_index]:
            merge_list.append(left_list[l_index])
            l_index += 1
        else:
            merge_list.append(right_list[r_index])
            r_index += 1
    # if l_index < len(left_list):
    merge_list += left_list[l_index:]
    # if r_index < len(right_list):
    merge_list += right_list[r_index:]
    return merge_list


list = [28, 32, 14, 12, 53, 42]
# 冒泡排序
# bubble_sort(list)
# 选择排序
# select_sort(list)
# 快速排序
# quick_sort(list,0,len(list)-1)
print(list)
sorted_list = merge_sort(list)
print("------排序结果-------")
print(sorted_list)
