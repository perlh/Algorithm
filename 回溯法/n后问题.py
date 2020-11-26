n = 8       #定义n为8的8皇后问题
x = [None]*n   # 定义n个空数组
sum  = 0  #用来保存结果的个数

def check(k):   #检查第k行是否满足条件。--非同行和同列，斜对角线
    global x
    global sum
    for i in range(k):
        if x[i] == x[k] or abs(x[i]-x[k]) == abs(i-k):
            return False
    return True

def backtrace(t):
    global n
    global sum
    global x
    if t > n-1:
        sum += 1
        print("结果:",end='')
        print(x)
    else:
        for i in range(n):
            x[t] = i
            if check(t):
                backtrace(t+1)
backtrace(0)   #0表示第一行
print("总共的解："+str(sum))

"""
例如4皇后问题
n=4

00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33

"""
