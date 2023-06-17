def rem(former, left, right):
    if left == 0:
        print(former, ")" * right, end="\n", sep="")
    else:
        if left < right:
            rem(former+"(", left - 1, right)
            rem(former+")", left, right - 1)
        else:
            rem(former + "(", left-1, right)


N = int(input())

if N % 2 != 0:
    exit(0)
else:
    rem("", N//2, N//2)
