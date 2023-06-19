def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result


def merge_sort(arr, lf, rg):
    if len(arr[lf:rg]) == 1:
        return arr[lf:rg]
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr[lf:rg] = merge(arr, lf, mid, rg)


def main():
    print(merge_sort([18, -19, 15, -8, 14, 6, -6, 8, 17], 0, 8))


if __name__ == '__main__':
    main()
