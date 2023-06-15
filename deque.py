"""ID 88235750."""
from typing import Type, List, Union


class Deque:
    """Class deque."""

    def __init__(self, max_n: int):
        self.queue = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        """Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise
        """
        return self.size == 0

    def is_full(self) -> bool:
        """Checks if the deque is full.

        Returns:
            bool: True if the deque is full, False otherwise
        """
        return self.size == self.max_n

    def push_back(self, item: int) -> None:
        """Adds an element to the end of the deque.

        Args:
            item (int): Element to be added to the end of the deque
        """
        if self.is_full():
            print('error')
        else:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def push_front(self, item: int) -> None:
        """Adds an element to the front of the deque.

        Args:
            item (int): Element to be added to the front of the deque
        """
        if self.is_full():
            print('error')
        else:
            self.queue[self.head - 1] = item
            self.head = (self.head - 1) % self.max_n
            self.size += 1

    def pop_back(self) -> Union[int, str]:
        """Outputs the last element of the deque and delete it.

        Returns:
            int: Integer value
        """
        if self.is_empty():
            return 'error'
        item = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return item

    def pop_front(self) -> Union[int, str]:
        """Outputs the front element of the deque and delete it.

        Returns:
            int: Integer value
        """
        if self.is_empty():
            return 'error'
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return item


def work_with_deque(deque: Type[Deque], command_list: List[List[str]]) -> None:
    """Function to work with deque

    Args:
        deque (Type[Deque]): Class Deque
        command_list (tuple): Tuples of commands for deque
    """
    for command in command_list:
        if len(command) > 1:
            if command[0] == 'push_front':
                deque.push_front(int(command[1]))
            if command[0] == 'push_back':
                deque.push_back(int(command[1]))
        else:
            if command[0] == 'pop_front':
                print(deque.pop_front())
            if command[0] == 'pop_back':
                print(deque.pop_back())


def main() -> None:
    """Main function."""
    command_count: int = int(input())
    deque: Type[Deque] = Deque(int(input()))
    command_list: List[List[str]] = []

    for _ in range(command_count):
        item: str = input().split()
        command_list.append(item)

    work_with_deque(deque, command_list)


if __name__ == '__main__':
    main()
