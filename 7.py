def binary_search(array, value):
    '''
    Args:
        array (list): sorted array
        value (int): value to find the index
        
    Returns:
        index (int): array[index - 1] < value <= array[index]
    '''
    left = -1
    right = len(array)

    while right - left > 1:
        center = (left + right) // 2
        if array[center] == value:
            return center
        elif array[center] < value:
            left = center
        else:
            right = center

    return right


def merge_sort(array):
    n = len(array)
    if n == 1:
        return array
    left = array[:(n//2)]
    left = merge_sort(left)
    right = array[(n//2):]
    right = merge_sort(right)

    ans = []
    i_l, i_r = 0, 0

    while True:
        if i_l < len(left):
            if i_r < len(right):
                if left[i_l] < right[i_r]:
                    ans.append(left[i_l])
                    i_l += 1
                else:
                    ans.append(right[i_r])
                    i_r += 1
            else:
                ans += left[i_l:]
                break
        else:
            if i_r < len(right):
                ans += right[i_r:]
                break
            else:
                break
    return ans


def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if data[i] < data[j]:
            data_temp.append(data[i])
            i = i + 1
        else:
            data_temp.append(data[j])
            j = j + 1

    while i <= mid:
        data_temp.append(data[i])
        i = i + 1

    while j <= end:
        data_temp.append(data[j])
        j = j + 1

    k = start
    for val in data_temp:
        data[k] = val
        k = k + 1  

def merge_sort_b(data, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort_b(data, start, mid)
    merge_sort_b(data, mid + 1, end)
    merge(data, start, mid, end)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    merge_sort_b(A, 0, len(A)-1)

    for _ in range(Q):
        b = int(input())
        b_ind = binary_search(A, b)
        if b_ind == len(A):
            print(b - A[-1])
        elif b_ind == 0:
            print(A[0] - b)
        else:
            print(min([b - A[b_ind - 1], A[b_ind] - b]))
