mod = 10**9 + 7

N, B, K = map(int, input().split())

C = list(map(int, input().split()))
C.sort()

# figure dp
dp = [[0 for _ in range(B)] for _ in range(N+1)]   # dp[i][j]... i桁の数で、Bで割った余りがjとなるようなものの通り数
for c in C:
    dp[1][c % B] += 1

for i in range(2, N+1):
    for j in range(B):
        for c in C:
            rem = (j * 10 + c) % B
            dp[i][rem] += dp[i-1][j]
            dp[i][rem] %= mod

print(dp[N][0])
# O(NBK)
