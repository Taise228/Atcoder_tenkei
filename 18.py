import numpy as np


def main():
    T = int(input())
    L, X, Y = map(int, input().split())

    Q = int(input())
    for _ in range(Q):
        E = int(input())
        angle = 2 * np.pi * E / T
        y = (-1) * (L / 2) * np.sin(angle) - Y
        z = (-1) * (L / 2) * np.cos(angle) + (L / 2)
        vec_a = np.array([-X, y, z])
        vec_b = np.array([-X, y, 0])
        # theta = np.rad2deg(np.arccos(np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))))
        denominator = np.sqrt(1 + ((L / 2) * (1 - np.cos(angle))) ** 2 / (X ** 2 + (Y + L / 2 * np.sin(angle)) ** 2))
        theta = np.rad2deg(np.arccos(1 / denominator))
        print(theta)


if __name__ == '__main__':
    main()
