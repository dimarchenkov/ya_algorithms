"""ID some 88200610"""
from typing import Callable, Dict, Type


class Stack:
    """Class representing stack"""

    def __init__(self):
        self.__operands = []
        self.__size = 0

    def push(self, item) -> None:
        """Add an item to the stack.

        Args:
            item (int): integer value
        """
        self.__size += 1
        self.__operands.append(item)

    def pop(self) -> int:
        """Outputs the first element of the stack and delete it.

        Returns:
            int: First item in the stack
        """
        if self.is_empty():
            return 'error'
        self.__size -= 1
        return self.__operands.pop()

    def is_empty(self) -> bool:
        """Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise
        """
        return self.__size == 0


def main() -> None:
    """Main function."""
    operations: Dict[str, Callable[[int, int], int]] = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }

    stack: Type[Stack] = Stack()

    for item in input().split():
        if item.lstrip('-').isdigit():
            stack.push(int(item))
        else:
            stack.push(operations[item](stack.pop(), stack.pop()))

    print(stack.pop())


if __name__ == '__main__':
    main()
