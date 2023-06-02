import bisect
import math


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

    vec_1 = [right[0] - centre[0], right[1] - centre[1]]
    vec_2 = [left[0] - centre[0], left[1] - centre[1]]

    length_1 = math.sqrt(vec_1[0] ** 2 + vec_1[1] ** 2)
    length_2 = math.sqrt(vec_2[0] ** 2 + vec_2[1] ** 2)
    inner_product = vec_1[0] * vec_2[0] + vec_1[1] * vec_2[1]
    cos = inner_product / (length_1 * length_2)

    rad = math.acos(cos)
    deg = math.degrees(rad)

    return deg


def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append([x, y])

    # calculate the maximum angle of three points
    max_angle = 0
    for i in range(N):
        centre = points[i]
        hor_angles = []

        for j in range(N):
            if i == j:
                continue
            if points[j][1] >= centre[1]:
                hor_angles.append(angle(centre, points[j], [centre[0] + 1, centre[1]]))
            else:
                hor_angles.append(360 - angle(centre, points[j], [centre[0] + 1, centre[1]]))

        hor_angles.sort()

        for j in range(N - 1):
            angle_1 = hor_angles[j]
            opp_angle = angle_1 + 180 if angle_1 < 180 else angle_1 - 180
            opp_ind = bisect.bisect_left(hor_angles, opp_angle)
            if opp_ind == len(hor_angles) or opp_ind == 0:
                if hor_angles[-1] - angle_1 > 180:
                    cand_1 = 360 - (hor_angles[-1] - angle_1)
                else:
                    cand_1 = hor_angles[-1] - angle_1
                if angle_1 - hor_angles[0] > 180:
                    cand_2 = 360 - (angle_1 - hor_angles[0])
                else:
                    cand_2 = angle_1 - hor_angles[0]
                ith_max_angle = max(cand_1, cand_2)
            else:
                if angle_1 < 180:
                    ith_max_angle = max(360 - (hor_angles[opp_ind] - angle_1), hor_angles[opp_ind - 1] - angle_1)
                else:
                    ith_max_angle = max(angle_1 - hor_angles[opp_ind], 360 - (angle_1 - hor_angles[opp_ind - 1]))

            max_angle = max(max_angle, ith_max_angle)

    print(max_angle)


if __name__ == '__main__':
    main()
