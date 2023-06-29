MOD = 10 ** 9 + 7


def modpow(a, b, m):
    """compute a^b mod m in O(log b)

    Args:
        a (int): base
        b (int): exponent
        m (int): divisor

    Returns:
        int: a^b mod m
    """

    p = 1
    q = a
    while b > 0:
        if b & 1:
            p = (p * q) % m
        q = (q * q) % m
        b >>= 1
    return p


def modinv(a, m):
    """compute a^-1 mod m in O(log m)
    a^-1 mod m = a^(m - 2) mod m

    Args:
        a (int): base
        m (int): divisor

    Returns:
        int: a^-1 mod m
    """
    return modpow(a, m - 2, m)


def fact_arr(n):
    """return [1!, 2!, ..., n!] mod MOD

    Args:
        n (int): the maximum number of factorial

    Returns:
        list: [1!, 2!, ..., n!] mod MOD
    """
    arr = [1] * n
    for i in range(1, n):
        arr[i] = (arr[i - 1] * (i + 1)) % MOD
    return arr


def inv_fact_arr(n):
    """return [1!^-1, 2!^-1, ..., n!^-1] mod MOD

    Args:
        n (int): the maximum number of factorial

    Returns:
        list: [1!^-1, 2!^-1, ..., n!^-1] mod MOD
    """

    arr = [1] * n
    arr[n - 1] = modinv(fact_arr(n)[n - 1], MOD)
    for i in range(n - 2, -1, -1):
        arr[i] = (arr[i + 1] * (i + 2)) % MOD
    return arr


def main():
    N = int(input())

    fact_mod = fact_arr(N)
    inv_fact_mod = inv_fact_arr(N)

    for k in range(1, N + 1):
        combinations = 0
        for a in range((N - 1) // k + 1):
            # combinations += {(N - (k - 1) * a) C (a + 1)} mod MOD
            # compute this in O(1)
            if N - k * a - 2 < 0:
                combinations += (fact_mod[N - (k - 1) * a - 1] * inv_fact_mod[a + 1 - 1]) % MOD
            else:
                combinations += ((fact_mod[N - (k - 1) * a - 1] * inv_fact_mod[a + 1 - 1] * inv_fact_mod[N - k * a - 2]) % MOD)

        print(combinations % MOD)


if __name__ == '__main__':
    main()
