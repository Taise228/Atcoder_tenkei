import numpy as np
import bisect


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
        centre = points[i]
        hor_angles = []

        for j in range(N):
            if i == j:
                continue
            if points[j][1] >= centre[1]:
                hor_angles.append(angle(centre, points[j], np.array([centre[0] + 1, centre[1]])))
            else:
                hor_angles.append(360 - angle(centre, points[j], np.array([centre[0] + 1, centre[1]])))

        hor_angles.sort()

        for j in range(N - 1):
            angle_1 = hor_angles[j]
            opp_angle = angle_1 + 180 if angle_1 < 180 else angle_1 - 180
            opp_ind = bisect.bisect_left(hor_angles, opp_angle)
            if opp_ind == len(hor_angles) or opp_ind == 0:
                ith_max_angle = max(hor_angles[-1] - angle_1, angle_1 - hor_angles[0])
            else:
                if angle_1 < 180:
                    ith_max_angle = max(360 - (hor_angles[opp_ind] - angle_1), hor_angles[opp_ind - 1] - angle_1)
                else:
                    ith_max_angle = max(angle_1 - hor_angles[opp_ind], 360 - (angle_1 - hor_angles[opp_ind - 1]))

            max_angle = max(max_angle, ith_max_angle)

    print(max_angle)


if __name__ == '__main__':
    main()
