#! /usr/bin/env python3
import random
def sort(a, l, r):           # 冒泡排序
    for i in range(l, r + 1):
        for j in reversed(range(i, r + 1)):
            if a[i] >= a[j]:
                a[i], a[j] = a[j], a[i]
def partition(a, left, right, x):     # 分区
    i = left
    j = right
    while i < j:
        while a[j] > x and i < j:
            j -= 1
        while a[i] < x and i < j:
            i += 1
        a[i], a[j] = a[j], a[i]
    return i


def find_mid(a, l, r):
    if r - l < 75:
        sort(a, l, r)
        return a[(l + r) // 2]
    else:
        b = []        # 存储中位数的数组
        i = l
        while True:
            if 5 * i + 4 <= r:         # 判断是否为最后一组
                sort(a, 5 * i, 5 * i + 4)
                b.append(a[5 * i + 2])
            else:
                sort(a, 5 * i, r)
                b.append(a[(5 * i + r) // 2])
                break
            i += 1
        return find_mid(b, 0, len(b) - 1)


def select(a, l, r, k):
    if r - l < 75:
        sort(a, l, r)
        return a[l + k - 1]
    else:
        mid_number = find_mid(a, l, r)
        mid_position = partition(a, l, r, mid_number)
        if k > mid_position:
            return select(a, mid_position + 1, r, k)
        else:
            return select(a, l, mid_position, k)


number = random.randint(50, 75)
array = []
for i in range(0, number):
    array.append(random.randint(0, number * 2))
print(array)
print("随机生成了" + str(number) + "个数")
k = input('输入想要第几小的数字:')
print(select(array, 0, number - 1, int(k)))
