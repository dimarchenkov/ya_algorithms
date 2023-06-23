"""ID 88490774"""
import random


class Intern:
    def __init__(self, name, points, fines):
        self.name = name
        self.points = points
        self.fines = fines

    def __gt__(self, other):
        if self.points == other.points:
            if self.fines == other.fines:
                return self.name < other.name
            else:
                return self.fines < other.fines
        else:
            return self.points > other.points

    def __lt__(self, other):
        if self.points == other.points:
            if self.fines == other.fines:
                return self.name > other.name
            else:
                return self.fines > other.fines
        else:
            return self.points < other.points


def effective_sort(arr, base_left, base_right):

    if base_left >= base_right:
        return -1

    left, right = base_left, base_right
    pivot = arr[random.randint(base_left, base_right)]

    while left < right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1
            #if arr[left][1] < arr[right][1]:
            #    arr[left], arr[right] = arr[right], arr[left]
            #if arr[left][1] == arr[right][1] and arr[left][2] > arr[right][2]:
            #    arr[left], arr[right] = arr[right], arr[left]
            #left += 1
            #right -= 1
    effective_sort(arr, base_left, right)
    effective_sort(arr, left, base_right)


def main():
    """Main func."""
    arr_len = int(input())
    arr = [input().split() for _ in range(arr_len)]
    interns = [Intern(i[0], int(i[1]), int(i[2])) for i in arr]

    effective_sort(interns, 0, arr_len-1)

    for intern in reversed(interns):
        print(intern.name)

def test():
    interns = [
        Intern('alla', 4, 100),
        Intern('gena', 6, 1000),
        Intern('gosha', 2, 90),
        Intern('rita', 2, 90),
        Intern('timofey', 4, 80),
    ]
    effective_sort(interns, 0, 4)
    print('\n')

    for intern in reversed(interns):
        print(intern.name)


if __name__ == '__main__':
    main()
    #test()
