def main():
    N = int(input())
    A = list(map(int, input().split()))

    # len(A) = 2 * N
    # extract the next elements from A until A becomes empty
    # at each step, the cost is |A[i] - A[i+1]|
    # find the minimum cost required to extract all elements from A

    # dp[i][j] = minimum cost required to extract A[i:j + 1]
    # j = i + 2 * n - 1 (n = natural number)
    # dp[i][j] =
    #   min(dp[i][k] + dp[k + 1][j] (k = i * 2 * m - 1, i + 1 <= k <= j - 2), dp[i + 1][j - 1] + |A[i] - A[j]|)

    dp = [[-1 for _ in range(2 * N)] for _ in range(2 * N)]

    for interval_length in range(1, 2 * N, 2):
        for i in range(2 * N - interval_length):
            j = i + interval_length
            if interval_length == 1:
                dp[i][j] = abs(A[i] - A[j])
                continue
            dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i + 1, j - 1, 2)] + [dp[i + 1][j - 1] + abs(A[i] - A[j])])

    print(dp[0][2 * N - 1])


if __name__ == '__main__':
    main()
