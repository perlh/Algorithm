def matrix_chain(matrixs):
    # 初始化calculation和split表
    calculation = []
    split = []
    for i in range(0, len(matrixs)):
        calculation.append([-1] * len(matrixs))
        split.append([-1] * len(matrixs))
        calculation[i][i] = 0
        split[i][i] = 0

    for i in range(1, len(matrixs)):
        for j in range(0, len(matrixs)):
            x = j
            y = j + i
            if y > len(matrixs) - 1:
                break
            least = matrixs[x][0] * matrixs[x][1] * matrixs[y][1] + calculation[x + 1][y]
            choice = x + 1

            for z in range(x + 1, y):
                # print(matrixs[z][1])
                if matrixs[z][1] != matrixs[z + 1][0]:
                    print("unvalid matrix chain")
                    return
                do = matrixs[x][0] * matrixs[z][1] * matrixs[y][1] + calculation[x][z] + calculation[z + 1][y]
                if do < least:
                    least = do
                    choice = z + 1
            calculation[x][y] = least
            split[x][y] = choice
    return calculation[0][len(matrixs) - 1],split

def TraceBack(i, j, s):#找出最优解
    if i==j:
         return 0
    else:
        print("添加括号的位置："+str(s[i-1][j-1]))
        TraceBack(i,s[i-1][j-1],s)
        TraceBack(s[i - 1][j - 1]+1,j,s)

def main():
    example = [[3, 9], [9, 5], [5, 6], [6, 12],[12,3]]
    print(example)
    Result,split =  matrix_chain(example)
    print("最优值：" + str(Result))
    TraceBack(1,5,split)
    a = [-1] * len(example)
main()
