"""Два велосипеда"""


def bin_search(arr, left, right, k):
    """_summary_

    Args:
        arr (_type_): _description_
        left (_type_): _description_
        right (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    if left > right:
        return -1

    mid = (left + right) // 2

    if k <= arr[mid]:
        if (k > arr[mid-1] or mid == 0):
            return mid + 1

        return bin_search(arr, left, mid-1, k)
    return bin_search(arr, mid+1, right, k)


def bike_count(arr, arr_len, bycicle_count):
    """_summary_

    Args:
        arr (_type_): _description_
        n (_type_): _description_
        bycicle_count (_type_): _description_

    Returns:
        _type_: _description_
    """
    first_buy = bin_search(arr, 0, (arr_len-1), bycicle_count)
    second_buy = bin_search(arr, 0, (arr_len-1), 2*bycicle_count)

    return first_buy, second_buy


def main():
    """Main function"""
    arr_len = int(input())
    arr = [int(num) for num in input().split(' ')]
    bycicle_count = int(input())

    print(*bike_count(arr, arr_len, bycicle_count))


if __name__ == '__main__':
    main()
