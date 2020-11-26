def BinarySearch(a,x,n):
    left = 0
    right = n-1
    while left<=right:
        middle = (right+left)//2
        if(x == a[middle]):
            return  middle
        if(x > a[middle]):
            left = middle + 1
        else:
            right = middle - 1
    return 0
arr = [1,2,4,5,7, 9, 18, 19, 21, 25]
n  = len(arr)
print(arr)
x = int(input("请输入一个数:"))
# x = 18
Result = BinarySearch(arr,x,n)
print(Result)
