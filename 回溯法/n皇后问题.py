num=0
def eight_queen(arr,finish_line=0):
    if finish_line == len(arr):                     #如果放置皇后成功的行数与数组中的元素个数一致（即棋盘的行数）则认为完成了一种摆法
        global num                                  #将上边定义的num定义为全局变量  这样才能在后边对其进行自加操作
        num+=1
        print("第%s种摆法：" % num)
        for i in range(n):
            # print("n="+str(n))
            print((i,arr[i]))

        return
        # break

    for stand in range(len(arr)):                   #对整个列进行扫描，将列标的标号赋值给数组中对应的元素
        arr[finish_line] = stand
        flag = True
        for line in range(finish_line):
            if arr[line] == stand or abs(arr[line]-stand) == finish_line-line:   #有皇后与当前放置的皇后处于同一列或同一斜线上
                flag = False
                # stand-=1
        if flag==True:
            eight_queen(arr,finish_line+1)
if __name__ == '__main__':
    n = 8
    eight_queen([None]*n)
    if num != 0:

        print("一共有%s种摆法" % num)
    else:
        print("无解")