import numpy as np


def angle(centre, right, left):
    """Calculate right-centre-left angle.

    Args:
        centre (np.array): Coordinates of centre point.
            shape: (2,) or (3,)
        right (np.array): Coordinates of right point.
            shape: (2,) or (3,)
        left (np.array): Coordinates of left point.
            shape: (2,) or (3,)

    Returns:
        (float): Angle degree of right-centre-left.
    """

    vec_1 = right - centre
    vec_2 = left - centre

    length_1 = np.linalg.norm(vec_1)
    length_2 = np.linalg.norm(vec_2)
    inner_product = np.dot(vec_1, vec_2)
    cos = inner_product / (length_1 * length_2)

    rad = np.arccos(cos)
    deg = np.rad2deg(rad)

    return deg


def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append(np.array([x, y]))

    # calculate the maximum angle of three points
    max_angle = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                angle_deg_1 = angle(points[i], points[j], points[k])
                angle_deg_2 = angle(points[j], points[k], points[i])
                angle_deg_3 = angle(points[k], points[i], points[j])
                max_angle = max(max_angle, angle_deg_1, angle_deg_2, angle_deg_3)

    print(max_angle)


if __name__ == '__main__':
    main()
