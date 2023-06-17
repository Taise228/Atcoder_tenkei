def main():
    N = int(input())
    arr = []
    max_d = 0
    for _ in range(N):
        d, c, s = map(int, input().split())
        arr.append([d, c, s])
        max_d = max(max_d, d)

    arr.sort(key=lambda x: x[0])

    opt = [[0 for _ in range(max_d + 1)] for _ in range(N + 1)]

    # dynamig programming
    # opt[i][j] = the maximum pay we can get from the first i jobs in j days

    # recurrence
    for i in range(1, N + 1):
        for j in range(max_d + 1):
            if j < arr[i - 1][1]:
                opt[i][j] = opt[i - 1][j]
            elif j > arr[i - 1][0]:
                opt[i][j] = opt[i][j - 1]
            else:
                opt[i][j] = max(opt[i - 1][j], opt[i - 1][j - arr[i - 1][1]] + arr[i - 1][2])

    # answer
    print(opt[N][max_d])


if __name__ == '__main__':
    main()
