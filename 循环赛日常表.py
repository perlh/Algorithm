def port(A,n):
    if n==1:#矩阵的长度为1， 这时候给最左上角的单元格赋值为1
        A[0][0]=1
        return
    port(A,n//2)
    m = n//2
    for i in range(m):
        for j in range(m):
            A[i][j + m] = A[i][j] + m #右上角的值 = 左上角的值 + 矩阵长度的一半
            A[i + m][j] = A[i][j + m] #右下角的值 = 左上角的值
            A[i + m][j + m] = A[i][j]  #左下角的值 = 右上角的值
mun = 8
matrix = [[0 for v in range(mun)] for v in range(mun)]  #创建二维数组
port(matrix,mun)
[print(i) for i in matrix]