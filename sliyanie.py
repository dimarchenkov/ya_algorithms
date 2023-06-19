def merge_sort(arr: list, left: int, right: int) -> None:

    if len(arr[left:right]) == 1:
        return arr[left:right]

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    arr[left:right] = merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int) -> list:
    left = arr[left:mid]
    right = arr[mid:right]
    result = [] # * len(arr)
    l, r, k = 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:] + right[r:]
    return result


def main():
    a = merge_sort([18, -19, 15, -8, 14, 6, -6, 8, 17], 0, 8)
    print(a)


if __name__ == '__main__':
    main()
