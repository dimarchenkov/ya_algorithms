"""ID some 88229901"""

from typing import Type


class Stack:
    """Class representing stack"""

    def __init__(self):
        self.items = []

    def push(self, item) -> None:
        """Add an item to the stack.

        Args:
            item (int): integer value
        """
        self.items.append(item)

    def pop(self) -> int:
        """Outputs the first element of the stack and delete it.

        Returns:
            int: First item in the stack
        """
        return self.items.pop()


def calc_function(stack: Type[Stack], expression: str) -> int:
    """Does calculations.

    Args:
        stack (Type[Stack]): Class stack
        expression (str): Expression in Danish notation

    Returns:
        int: Calculating result
    """

    for item in expression:
        if item not in ['+', '-', '/', '*']:
            stack.push(int(item))
        elif item in '*':
            stack.push(stack.pop() * stack.pop())
        elif item == '+':
            stack.push(stack.pop() + stack.pop())
        elif item == '-':
            second_argument = stack.pop()
            first_argument = stack.pop()
            stack.push(first_argument - second_argument)
        elif item == '/':
            second_argument = stack.pop()
            first_argument = stack.pop()
            stack.push(first_argument // second_argument)
    return stack.pop()


def main() -> None:
    """Main function."""
    stack: Type[Stack] = Stack()
    expression: str = input().split()
    print(calc_function(stack, expression))


if __name__ == '__main__':
    main()
