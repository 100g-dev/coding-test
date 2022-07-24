#q31 - 금광
# d[n, m] = max(d[n-1, m-1], d[n, m-1], d[n+1, m-1])


t = int(input())
for _ in range(t):

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    dp = []
    for i in range(0, len(data), m):
        dp.append(data[i:i+m])
    # print(dp) ##

    for j in range(1, m):
        for i in range(n):
            if i==0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]

            dp[i][j] += max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)