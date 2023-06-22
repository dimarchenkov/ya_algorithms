"""ID someID"""


def bin_search(arr, left, right, k):

    if left > right:
        return -1

    mid = (left + right) // 2

    if k == arr[mid]:
        return mid

    if arr[left] <= arr[mid]:
        return (
            bin_search(arr, left, mid - 1, k)
            if arr[left] <= k < arr[mid]
            else bin_search(arr, mid + 1, right, k)
        )
    return (
        bin_search(arr, mid+1, right, k)
        if arr[mid] < k <= arr[right]
        else bin_search(arr, left, mid-1, k)
    )


def broken_search(arr, k):

    if len(arr) == 1:
        return 0 if arr[0] == k else -1

    return bin_search(arr, 0, (len(arr)-1), k)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    print(broken_search(arr, 5))


if __name__ == '__main__':
    test()
