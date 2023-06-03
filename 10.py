def main():
    N = int(input())

    one_cumulative_sum = [0 for _ in range(N)]
    two_cumulative_sum = [0 for _ in range(N)]

    for i in range(N):
        c, p = map(int, input().split())
        if c == 1:
            if i == 0:
                one_cumulative_sum[i] = p
                two_cumulative_sum[i] = 0
            else:
                one_cumulative_sum[i] = one_cumulative_sum[i - 1] + p
                two_cumulative_sum[i] = two_cumulative_sum[i - 1]
        else:
            if i == 0:
                one_cumulative_sum[i] = 0
                two_cumulative_sum[i] = p
            else:
                one_cumulative_sum[i] = one_cumulative_sum[i - 1]
                two_cumulative_sum[i] = two_cumulative_sum[i - 1] + p

    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        if L == 0:
            print(one_cumulative_sum[R], two_cumulative_sum[R])
        else:
            print(one_cumulative_sum[R] - one_cumulative_sum[L - 1], two_cumulative_sum[R] - two_cumulative_sum[L - 1])


if __name__ == '__main__':
    main()
