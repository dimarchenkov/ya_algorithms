"""ID someID"""
def bin_search(arr, left, right, k):

    # if left > right:
    #     return -1

    # mid = (left + right) // 2

    # if k == arr[mid]:
    #     return mid
    # if k < arr[mid]:
    #     return bin_search(arr, left, mid-1, k)
    # if k > arr[mid]:
    #     return bin_search(arr, mid+1, right, k)
    # while left <= right:
    #     mid = (left + right) // 2

    #     if arr[mid] == k:
    #         return mid
    #     if arr[mid] < k:
    #         left = mid + 1
    #     elif arr[mid] > k:
    #         right = mid - 1
    # return -1
    if left > right:
        return -1

    mid = (left + right) // 2

    if k == arr[mid]:
        return mid

    if arr[left] <= arr[mid]:
        if arr[left] <= k < arr[mid]:
            return bin_search(arr, left, mid-1, k)
        else:
            return bin_search(arr, mid+1, right, k)
    else:

        if arr[mid] < k <= arr[right]:
            return bin_search(arr, mid+1, right, k)
        else:
            return bin_search(arr, left, mid-1, k)






def broken_search(arr, k) -> int:

    if len(arr) == 1:
        return 0 if arr[0] == k else -1

    # flag = False
    # for i in range(len(arr)-1):
    #     if arr[i] > arr[i+1]:
    #         right = i
    #         flag = True
    #         break

    #if flag is False:
    return bin_search(arr, 0, (len(arr)-1), k)

    # if len(arr[:right+1]) < len(arr[right+1:]):
    #result_1 = bin_search(arr[:right+1], 0, right, k)
    #if result_1 != -1:
    #    return result_1

    # if len(arr[:right+1]) > len(arr[right+1:]):
    #     result_2 = bin_search(arr[right+1:], 0, (len(arr[right+1:])-1), k)
    #     if result_2 != -1:
    #         return result_2+right+1

    # result_1 = bin_search(arr[:right+1], 0, right, k)
    # return result_1


def main():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    arr = [9, 1, 3, 8]
    arr = [3, 6, 7]
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    arr = [5, 1]
    arr = [9, 1, 3, 8]
    print(broken_search(arr, 8))


if __name__ == '__main__':
    main()
