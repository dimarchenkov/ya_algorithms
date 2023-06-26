"""ID 88522664"""


def bin_search(arr: list[int], left: int, right: int, k: int) -> int:
    """Binary search fuction"""

    if left > right:
        return -1

    mid = (left + right) // 2
    mid_value = arr[mid]

    if k == mid_value:
        return mid

    if arr[left] <= mid_value:
        return (
            bin_search(arr, left, mid - 1, k)
            if arr[left] <= k < mid_value
            else bin_search(arr, mid + 1, right, k)
        )
    return (
        bin_search(arr, mid+1, right, k)
        if mid_value < k <= arr[right]
        else bin_search(arr, left, mid-1, k)
    )


def broken_search(arr: list[int], k: int) -> int:
    """Broken arr search funtion"""
    if len(arr) == 1 and arr[0] != k:
        return -1

    return bin_search(arr, 0, (len(arr)-1), k)


def main() -> None:
    """Main function."""
    searching_element: int = int(input())
    arr: list[int] = [int(n) for n in input().split()]
    print(broken_search(arr, searching_element))


def test() -> None:
    """Test function."""
    def _testing(arr, searching_element, right_answer):
        result: list = arr
        assert broken_search(result, searching_element) == right_answer
        print(f'Test passed for {arr}')

    _testing([19, 21, 100, 101, 1, 4, 5, 7, 12], 5, 6)
    _testing([18], 18, 0)
    _testing([3], 19, -1)


if __name__ == '__main__':
    test()
    main()
