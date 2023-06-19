def comporator(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    variant_1 = number_1 + number_2
    variant_2 = number_2 + number_1
    return variant_1 > variant_2


def big_number(arr, n):
    for i in range(n):
        item_to_insert = arr[i]
        j = i
        while j > 0 and comporator(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
            arr[j] = item_to_insert
    return arr


def main():
    n = int(input())
    arr = input().split()
    result = big_number(arr, n)
    total = ''.join(str(i) for i in result)
    print(total)


if __name__ == '__main__':
    main()
