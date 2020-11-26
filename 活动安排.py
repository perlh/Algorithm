#! /usr/bin/env python3
# 用冒泡排序对结束时间进行排序，同时得到对应的开始时间的list
def bubble_sort(s, f):
    for i in range(len(f)):
        for j in range(0, len(f) - i - 1):
            if f[j] > f[j + 1]:
                f[j], f[j + 1] = f[j + 1], f[j]
                s[j], s[j + 1] = s[j + 1], s[j]
    return s, f



1
def greedy(s, f, n):
    a = [True for x in range(n)]
    # 初始选择第一个活动
    j = 0
    for i in range(1, n):
        # 如果下一个活动的开始时间大于等于上个活动的结束时间
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a


# n = int(input("请输入活动的个数："))
curriculum = "(1,2) (6,8) (3,5) (7,8) (2,3) (7,9) (8,10) (10,11)"
arr = curriculum.split()
n  = len(arr)
print(arr)

s = []

f = []
for ar in arr:
    ar = ar[1:-1]
    start = int(ar.split(',')[0])
    end = int(ar.split(',')[1])
    s.append(start)
    f.append(end)
print(s)
print(f)
s, f = bubble_sort(s, f)
A = greedy(s, f, n)

res = []
for k in range(len(A)):
    if A[k]:
        res.append('({},{})'.format(s[k], f[k]))
print(' '.join(res))
