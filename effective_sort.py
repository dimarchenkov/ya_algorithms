"""ID 88522868"""
import random
from dataclasses import dataclass


@dataclass
class Intern:
    """Class for interns."""
    name: str
    points: int
    fines: int

    def __repr__(self) -> str:
        """Reruns string representation of an object."""
        return self.name

    # без конвертации в int: bad operand type for unary -: 'str'
    # если конвертить в lt получаем TL на
    def __post_init__(self) -> None:
        """Converting str to int."""
        self.points = int(self.points)
        self.fines = int(self.fines)

    def __lt__(self, other) -> bool:
        """Comparison function."""
        return (
            (-self.points, self.fines, self.name)
            < (-other.points, other.fines, other.name)
        )


def effective_sort(arr: list) -> None:
    """Efficient sorting algorithm."""
    def _eff_sort(left_board: int, right_board: int):
        if left_board >= right_board:
            return -1

        left: int = left_board
        right: int = right_board
        pivot: int = arr[random.randint(left, right)]

        while left < right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
                left += 1

        _eff_sort(left_board, right)
        _eff_sort(left, right_board)

    return _eff_sort(0, len(arr)-1)


def main() -> None:
    """Main func."""
    arr_len: int = int(input())
    arr: list = [Intern(*input().split()) for _ in range(arr_len)]
    effective_sort(arr)
    print(*arr, sep='\n')


def test() -> None:
    """Testing and debugging function."""
    interns: Intern = [
        Intern('alla', '0', '0'),
        Intern('gena', '0', '1000'),
        Intern('gosha', '2', '0'),
        Intern('rita', '2', '90'),
        Intern('timofey', '4', '80'),
    ]
    effective_sort(interns)
    print(*interns, sep='\n')


if __name__ == '__main__':
    main()
    # test()
