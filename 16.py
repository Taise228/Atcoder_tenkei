def main():
    N = int(input())
    A, B, C = map(int, input().split())

    min_count = 10 ** 4
    L = 9999

    for i in range(L + 1):
        for j in range(L + 1 - i):
            k = N - (A * i + B * j)
            if k % C == 0 and k >= 0:
                count = i + j + k // C
                min_count = min(min_count, count)

    print(min_count)


if __name__ == '__main__':
    main()
