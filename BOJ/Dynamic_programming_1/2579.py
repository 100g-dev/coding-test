#2579 - 계단 오르기

# f(n) = S_n + f(n-3) + max(S_{n-2}, S_{n-1})

n = int(input())
score = []
for i in range(n):
    score.append(int(input()))

dp = [0]*301
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0], score[1])+ score[2]
for i in range(3, n):
    dp[i] = max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])

print(dp[n-1])