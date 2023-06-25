def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    sum = 0
    for i in range(N):
        sum += abs(A[i] - B[i])

    print(sum)


if __name__ == '__main__':
    main()
