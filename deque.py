"""ID 88195334."""
from typing import Tuple, Type


class NoItemsError(Exception):
    """Class for empty items."""

    def __init__(self):
        pass


class StackOverflowError(Exception):
    """Class for stack overflow."""
    def __init__(self):
        pass


class Deque:
    """Class deque."""

    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    def push_back(self, item) -> None:
        """Adds an element to the end of the deque.

        Args:
            item (int): Element to be added to the end of the deque

        Raises:
            StackOverflowError: If the maximum number of elements
            is already in the deck, outputs "error".
        """
        if self.is_full():
            raise StackOverflowError
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__queue[self.__tail] = item
        self.__size += 1

    def push_front(self, item) -> None:
        """Add an element to the front of the deque.

        Args:
            item (int): Element to be added to the front of the deque

        Raises:
            StackOverflowError: If the maximum number of elements
            is already in the deck, outputs "error".
        """
        if self.is_full():
            raise StackOverflowError
        self.__head = (self.__head - 1) % self.__max_size
        self.__queue[self.__head] = item
        self.__size += 1

    def pop_front(self) -> int:
        """Outputs the first element of the deque and delete it.

        Raises:
            NoItemsError: _description_

        Returns:
            int: First element of the deck
        """
        if self.is_empty():
            raise NoItemsError
        item = self.__queue[self.__head]
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return item

    def pop_back(self) -> int:
        """Outputs the last element of the deque and delete it.

        Raises:
            NoItemsError: _description_

        Returns:
            int: Last element of the deck
        """
        if self.is_empty():
            raise NoItemsError
        item = self.__queue[self.__tail]
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size -= 1
        return item

    def is_empty(self) -> bool:
        """Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise
        """
        return self.__size == 0

    def is_full(self) -> bool:
        """Checks if the deque is full.

        Returns:
            bool: True if the deque is full, False otherwise
        """
        return self.__size == self.__max_size


def get_input() -> Tuple[int, int]:
    """Get the input. Returns length_street and coordinates.

    Returns:
        Tuple[int, int]: Data from the input
    """
    command_count: int = int(input())
    max_size: int = int(input())
    return command_count, max_size


def main() -> None:
    """Main function."""
    command_count, max_size = get_input()
    deque: Type[Deque] = Deque(max_size)
    for _ in range(command_count):
        try:
            item = input().split()
            if len(item) == 1:
                print(getattr(deque, item[0])())
            else:
                getattr(deque, item[0])(item[1])
        except (NoItemsError, StackOverflowError):
            print('error')


if __name__ == '__main__':
    main()
