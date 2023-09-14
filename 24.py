def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dif_sum = 0
    for i in range(N):
        dif_sum += abs(A[i] - B[i])

    if K >= dif_sum and (K - dif_sum) % 2 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
