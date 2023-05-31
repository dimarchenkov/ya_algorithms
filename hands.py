# ID 87826952
def get_input() -> tuple[int, str]:
    """
    Get the input. Returns k - count of keys
    and sequence of values.
    """
    k: int = int(input()) * 2
    sequence: str = ''.join([input() for _ in range(4)])
    return k, sequence


def get_score(k: int, sequence: str) -> int:
    """Get the score."""
    unique_of_sequence: set = set(sequence)
    keys_count: dict = {element: 0 for element in unique_of_sequence}

    for element in sequence:
        keys_count[element] += 1

    for key in unique_of_sequence:
        if key == '.' or keys_count[key] > k:
            del keys_count[key]

    return len(keys_count)


def main() -> None:
    """Main program."""
    k: int = 0
    sequence: str = ''
    k, sequence = get_input()
    print(get_score(k, sequence))


if __name__ == '__main__':
    main()
