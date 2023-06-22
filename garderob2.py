"""гардероб"""


def sort(arr):
    """_summary_

    Args:
        arr (_type_): _description_

    Returns:
        _type_: _description_
    """
    counted_values = [0] * 3
    for elem in arr:
        counted_values[elem] += 1
    index = 0

    for value in range(3):
        for _ in range(counted_values[value]):
            arr[index] = value
            index += 1
    return arr


def main():
    """Main func."""
    # arr_len = int(input())
    arr = list(map(int, input().split()))
    print(*sort(arr))


if __name__ == '__main__':
    main()
