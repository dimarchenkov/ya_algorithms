'''ID 87846776'''
from typing import Tuple, Dict, Set


def get_input() -> Tuple[int, str]:
    """Get data fromthe input.

    Returns:
        Tuple[int, str]: Data from the input
    """
    k: int = int(input()) * 2
    sequence: str = ''.join([input() for _ in range(4)])
    return k, sequence


def get_score(k: int, sequence: str) -> int:
    """Get the score.

    Args:
        k (int): The number of buttons that players can press
        sequence (str): String of Playing field

    Returns:
        int: Final score of the game
    """
    keys_count: Dict[str, int] = {}
    outsiders: Set[str] = {'.', }
    for element in sequence:
        if element not in outsiders:
            if element not in keys_count:
                keys_count[element] = 1
            else:
                keys_count[element] += 1

            if keys_count[element] > k:
                del keys_count[element]
                outsiders.add(element)

    return len(keys_count)


def main() -> None:
    """Main program."""
    k, sequence = get_input()
    print(get_score(k, sequence))


if __name__ == '__main__':
    main()
