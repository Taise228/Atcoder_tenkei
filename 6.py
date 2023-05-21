if __name__ == '__main__':

    N, K = map(int, input().split())
    S = input()

    optimal = S[N-K:]

    for idx in range(N-K-1, -1, -1):
        char = S[idx]
        if char <= optimal[0]:
            change = 0
            while True:
                if change == K-1:
                    optimal = char + optimal[:K-1]
                    break
                if optimal[change] > optimal[change+1]:
                    optimal = char + optimal[:change] + optimal[change+1:]
                    break
                change += 1
    
    print(optimal)