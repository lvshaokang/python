#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def bubbleSort(arr):
    length = len(arr)
    for i in range(0, length - 1):
        for j in range(0, length - 1 - i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionSort(arr):
    length = len(arr)
    # temp = []
    for i in range(0, length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if (arr[j] < arr[minIndex]):
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]

    return arr


def insertionSort(arr):
    length = len(arr)
    for i in range(1, length):
        preIndex = i - 1
        current = arr[i]
        while (preIndex >= 0 and arr[preIndex] > current):
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current

    return arr


def shellSort(arr):
    length = len(arr)
    gap = 1
    while (gap < length / 3):
        gap = gap * 3 + 1

    while (gap > 0):
        gap = math.floor(gap / 3)
        for i in range(gap, length):
            temp = arr[i]
            j = i - gap
            while (j > 0 and arr[j] > temp):
                arr[j + gap] = arr[j]
                j = j - gap
            arr[j + gap] = temp

    return arr


def quick_sort(arr, start, end):
    if start >= end:
        return
    low_index = start
    high_index = end

    basic = arr[start]
    while low_index < high_index:
        while low_index < high_index and arr[high_index] >= basic:
            high_index -= 1

        if low_index != high_index:
            arr[low_index] = arr[high_index]
            low_index += 1
        print(arr)

        while low_index < high_index and arr[low_index] < basic:
            low_index += 1

        if low_index != high_index:
            arr[high_index] = arr[low_index]
            high_index -= 1
        print(arr)

    arr[low_index] = basic
    quick_sort(arr, start, low_index - 1)
    quick_sort(arr, high_index + 1, end)
    return arr


list = [28, 32, 14, 12, 53, 42]
# print(bubbleSort([1,5,3,2]))
# print(selectionSort([1,5,3,2]))
# print(insertionSort([1,5,3,2]))
# print(shellSort([1,5,3,2]))
quick_sort(list, 0, len(list) - 1)
# print()
