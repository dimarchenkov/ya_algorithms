"""ID 88266184."""
from collections.abc import Callable


class Deque:
    """Class deque."""

    def __init__(self, max_n: int):
        self.__queue = [None] * max_n
        self.__max_n = max_n
        self.__head = 0
        self.__tail = 0
        self.__size = 0

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
        return self.__size == self.__max_n

    def __index_calc(self, head_or_tail: int, __sum=True) -> int:
        """Calculates the index of the head or tail of the deque.

        Args:
            head_or_tail (int): tail or head of the deque
            __sum (bool, optional): Sum if true, subtraction if false

        Returns:
            int: Integer value of the index of the head or tail
        """
        return (
            (head_or_tail + 1) % self.__max_n if __sum
            else (head_or_tail - 1) % self.__max_n
        )

    def push_back(self, item: int) -> None:
        """Adds an element to the end of the deque.

        Raises:
            OverflowError: If the queue is full

        Args:
            item (int): Element to be added to the end of the deque
        """
        if self.is_full():
            raise OverflowError
        self.__queue[self.__tail] = item
        self.__tail = self.__index_calc(self.__tail)
        self.__size += 1

    def push_front(self, item: int) -> None:
        """Adds an element to the front of the deque.

        Raises:
            OverflowError: If the queue is full

        Args:
            item (int): Element to be added to the front of the deque
        """
        if self.is_full():
            raise OverflowError
        self.__queue[self.__head - 1] = item
        self.__head = self.__index_calc(self.__head, False)
        self.__size += 1

    def pop_back(self) -> int:
        """Outputs the last element of the deque and delete it.

        Raises:
            IndexError: Raised when a sequence subscript is out of range.

        Returns:
            int: Value of the last element of the deque
        """
        if self.is_empty():
            raise IndexError
        item = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = self.__index_calc(self.__tail, False)
        self.__size -= 1
        return item

    def pop_front(self) -> int:
        """Outputs the front element of the deque and delete it.

        Raises:
            IndexError: Raised when a sequence subscript is out of range.

        Returns:
            int: Integer value
        """
        if self.is_empty():
            raise IndexError
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.__index_calc(self.__head)
        self.__size -= 1
        return item


def work_with_deque(deque: Deque, command_count: int) -> None:
    """Function to work with deque

    Args:
        deque (Type[Deque]): Class Deque
        command_list (tuple): Tuples of commands for deque
    """
    slovar: dict[str, Callable] = {
        'push_front': deque.push_front,
        'push_back': deque.push_back,
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
    }

    for _ in range(command_count):
        first, *rest = input().split()
        try:
            slovar[first](int(*rest)) if rest else print(slovar[first]())
        except (OverflowError, IndexError):
            print('error')


def main() -> None:
    """Main function."""
    command_count: int = int(input())
    deque: Deque = Deque(int(input()))
    work_with_deque(deque, command_count)


if __name__ == '__main__':
    main()
