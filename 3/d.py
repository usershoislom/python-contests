def count(n):
    dp = [[0]*3 for i in range(n+1)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1

    for i in range(2, n+1):
        for j in range(3):
            for k in range(3):
                if (j != 2) or (k != 2):
                    dp[i][j] += dp[i-1][k]

    return sum(dp[n])

print(count(int(input())))