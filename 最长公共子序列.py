# 使用备忘录的
def longestCommonSubsequence(str1, str2) -> int:
    m, n = len(str1), len(str2)
    # 构建 DP table 和 base case
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 进行状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(dp)
            if str1[i - 1] == str2[j - 1]:
                # 找到一个 lcs 中的字符
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    for  i in dp:
        print(i)
    return dp[-1][-1]

a = 'acegzbdcdcddzguouo'
b = 'ababbabcecsdaf'
test = longestCommonSubsequence(a,b)
print(test)