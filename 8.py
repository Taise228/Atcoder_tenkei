if __name__ == '__main__':
    N = int(input())
    S = input()

    r = [0 for _ in range(N + 1)]
    er = [0 for _ in range(N + 1)]
    der = [0 for _ in range(N + 1)]
    oder = [0 for _ in range(N + 1)]
    coder = [0 for _ in range(N + 1)]
    tcoder = [0 for _ in range(N + 1)]
    atcoder = [0 for _ in range(N + 1)]

    for i in range(N-1, -1, -1):
        if S[i] == 'r':
            r[i] = r[i + 1] + 1
            er[i] = er[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1]
        elif S[i] == 'e':
            r[i] = r[i + 1]
            er[i] = er[i + 1] + r[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1]
        elif S[i] == 'd':
            r[i] = r[i + 1]
            er[i] = er[i + 1]
            der[i] = der[i + 1] + er[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1]
        elif S[i] == 'o':
            r[i] = r[i + 1]
            er[i] = er[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1] + der[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1]
        elif S[i] == 'c':
            r[i] = r[i + 1]
            er[i] = er[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1] + oder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1]
        elif S[i] == 't':
            r[i] = r[i + 1]
            er[i] = er[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1] + coder[i + 1]
            atcoder[i] = atcoder[i + 1]
        elif S[i] == 'a':
            r[i] = r[i + 1]
            er[i] = er[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1] + tcoder[i + 1]
        else:
            r[i] = r[i + 1]
            er[i] = er[i + 1]
            der[i] = der[i + 1]
            oder[i] = oder[i + 1]
            coder[i] = coder[i + 1]
            tcoder[i] = tcoder[i + 1]
            atcoder[i] = atcoder[i + 1]
    print(atcoder[0] % ((10 ** 9) + 7))
