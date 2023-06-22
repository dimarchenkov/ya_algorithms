"""B. Комбинации"""


def reqursion(arr, tel_numbers):

    if arr == '':
        return ['']

    result = []
    numbers = tel_numbers[arr[-1]]

    for i in reqursion(arr[:-1], tel_numbers):
        result.extend(i + j for j in numbers)
    return result

def combinations(arr):
    tel_numbers = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    return reqursion(arr, tel_numbers)


def main():
    """Main func."""
    arr = input()

    print(combinations(arr))


if __name__ == '__main__':
    main()
