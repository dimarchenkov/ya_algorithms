'''ID 87851006'''
from typing import Tuple, List, Optional, Union


def get_input() -> Tuple[int, List[int]]:
    """Get the input. Returns length_street and coordinates.

    Returns:
        Tuple[int, List[int]]: Data from the input
    """
    length_street: int = int(input())
    coordinates: list[int] = [
        int(x) for x in input().split()
    ]
    return length_street, coordinates


def get_zero_distance(
    length_street: int,
    coordinates: List[int]
) -> List[Union[int, float]]:
    """Returns the distance to the nearest zero.

    Args:
        length_street (int): Length of the street
        coordinates (List[int]): Coordinates

    Returns:
        List[Union[int, float]]: Distance to the nearest zero
    """
    distance: List[Union[int, float]] = [float('inf')] * length_street
    zero_position: Optional[int] = None
    for i, elem in enumerate(coordinates):
        if elem == 0:
            zero_position = i
            distance[i] = 0
            continue

        distance[i] = (
            (i - zero_position) if zero_position is not None else length_street
        )
    zero_position = None

    for i, elem in reversed(list(enumerate(coordinates))):
        if elem == 0:
            zero_position = i
            continue
        if zero_position is not None and distance[i] > zero_position - i:
            distance[i] = zero_position - i

    return distance


def main() -> None:
    """Main program."""
    length_street: int = 0
    coordinates: list[int] = []
    length_street, coordinates = get_input()
    print(*get_zero_distance(length_street, coordinates))


if __name__ == '__main__':
    main()
