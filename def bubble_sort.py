def bubble_sort(arr, n):
    counter = True
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter = True

        if counter:
            print(*arr)
            counter = False


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    bubble_sort(arr, n)


if __name__ == '__main__':
    main()
