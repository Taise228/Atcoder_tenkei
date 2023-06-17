N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# scoreは0以上L以下 -> この範囲で二分探索する
# (例)答えはL以下か? yes -> 答えはL/2以下か? no -> 答えは3L/4以下か? no -> ...
# 答えはx以下か?を判定するのはO(N)でできる


def possible(A, x, L, K):
    # 長さx以上のK+1ピースに分割
    # 最後に残りの切れ端もx以上か確認
    num = 0
    now = 0
    for i in range(len(A)):
        if i == len(A) - 1:
            if A[i] - now >= x and L - A[i] >= x:
                num += 2
            else:
                num += 1
        elif A[i] - now >= x and L - A[i] >= x:
            now = A[i]
            num += 1
    if num >= K + 1:
        return True
    else:
        return False


maximum = L
minimum = 0
while maximum > minimum:
    center = (maximum + minimum) // 2
    if possible(A, center, L, K):
        if minimum == center:
            # この時点でmaximum = minimum + 1
            break
        minimum = center
    else:
        maximum = center

print(minimum)
