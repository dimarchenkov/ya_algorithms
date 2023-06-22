"""ID some ID"""
import random

def find_pivot(arr):
    if len(arr) < 5:
        return random.randint(arr[0], arr[len(arr)-1])
    arr_pivots = [0] * 3
    arr_pivots[0] = arr[0]
    arr_pivots[1] = arr[len(arr)//2]
    arr_pivots[2] = arr[len(arr)-1]
    for i in range(2):
        for j in range(2-i):
            if arr_pivots[j] > arr_pivots[j+1]:
                arr_pivots[j], arr_pivots[j+1] = arr_pivots[j+1], arr_pivots[j]
    return arr_pivots[1]

# def partition(arr, pivot):
#     left, right, center = [], [], []
#     for i, elem in enumerate(arr):
#         if elem < pivot:
#             left.append(arr[i])
#         if elem == pivot:
#             center.append(arr[i])
#         if elem > pivot:
#             right.append(arr[i])

#     return left, center, right


def effective_sort(arr, low, high):

    # if arr_len < 2:
    #     return arr

    # pivot = find_pivot(arr)
    # left = 0
    # right = arr_len-1

    # while left != right:
    #     while arr[left] < pivot:
    #         left += 1

    #     while arr[right] > pivot:
    #         right -= 1

    #     if arr[left] > arr[right]:
    #         arr[left], arr[right] = arr[right], arr[left]

    # effective_sort(arr[:left], len(arr[:left]))
    # effective_sort(arr[right:], len(arr[right:]))

    if low >= high:
        return -1

    left, right = low, high
    pivot = arr[random.randint(low, high)]

    while left < right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    effective_sort(arr, low, right)
    effective_sort(arr, left, high)
    print(arr)


def main():
    """Main func."""
    # arr_len = int(input())
    arr = [1, 4, 5, 6, 3, 2, 9]
    # arr = list(map(int, input().split()))

    effective_sort(arr, 0, 6)
    print(arr)
    # for name in result:
    #    print(name)


if __name__ == '__main__':
    main()
