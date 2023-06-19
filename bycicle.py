def stoumost(arr, bycicle_count, left, right, result):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= (bycicle_count * 2):
        result[1] = mid
        return mid+1
    elif arr[mid] >= bycicle_count:
        result[0] = mid
        return mid+1
    elif bycicle_count < arr[mid]:
        return stoumost(arr, bycicle_count, left, mid, result)
    else:
        return stoumost(arr, bycicle_count, mid+1, right, result)


def main():
    n = int(input())
    arr = [int(num) for num in input().split(' ')]
    bycicle_count = int(input())

    left = 0
    right = n

    result = stoumost(arr, bycicle_count, left, right, result=[-1, -1])
    print(*result)


if __name__ == '__main__':
    main()
