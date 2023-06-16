"""ID 88266245"""

import operator
from typing import Dict, Callable


class Stack:
    """Class representing stack"""

    def __init__(self):
        self.__items = []

    def push(self, item: int) -> None:
        """Add an item to the stack.

        Args:
            item (int): integer value
        """
        self.__items.append(item)

    def pop(self) -> int:
        """Outputs the first element of the stack and delete it.

        Returns:
            int: First item in the stack
        """
        return self.__items.pop()

    def peek(self) -> int:
        """Outputs the first element of the stack

        Returns:
            int: First item in the stack
        """
        return self.__items[-1]


def calc_function(stack: Stack, expression: str) -> int:
    """Does calculations.

    Args:
        stack (Type[Stack]): Class stack
        expression (str): Expression in Danish notation

    Returns:
        int: Calculating result
    """

    operations: Dict[str, Callable[[int, int], int]] = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.floordiv,
        '*': operator.mul,
    }

    for item in expression:
        if item not in operations:
            stack.push(int(item))
        else:
            second_argument, first_argument = stack.pop(), stack.pop()
            stack.push(operations[item](first_argument, second_argument))
    return stack.peek()


def main() -> None:
    """Main function."""
    stack: Stack = Stack()
    expression: list = input().split()
    print(calc_function(stack, expression))


if __name__ == '__main__':
    main()
