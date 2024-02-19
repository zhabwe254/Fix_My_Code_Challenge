#!/usr/bin/python3
""" FizzBuzz
"""

import sys


def fizzbuzz(n, *, start=1, end=None):
    """
    FizzBuzz function prints numbers from `start` (inclusive) to `end` (exclusive)
    separated by spaces.

    - For multiples of `3`, prints "Fizz" instead of the number.
    - For multiples of `5`, prints "Buzz" instead of the number.
    - For numbers that are multiples of both `3` and `5`, prints "FizzBuzz" instead of the number.
    - Otherwise, prints the number itself.

    Args:
        n (int): The upper limit (exclusive) of the range to print.
        start (int, optional): The lower limit (inclusive) of the range to print. Defaults to 1.
        end (int, optional): The upper limit (exclusive) of the range to print. If not provided,
                defaults to `n + 1`.

    Returns:
        None
    """

    if n < start:
        raise ValueError("n must be greater than or equal to start")

    if end is None:
        end = n + 1

    # Use string formatting for efficiency and clarity
    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    result = []
    for i in range(start, end):
        output = (
            fuzzbuzz if i % 3 == 0 and i % 5 == 0 else
            fizz if i % 3 == 0 else
            buzz if i % 5 == 0 else
            str(i)
        )
        result.append(output)

    print(" ".join(result))


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        if len(sys.argv) > 2:
            start = int(sys.argv[2])
            if len(sys.argv) > 3:
                end = int(sys.argv[3])
        fizzbuzz(n, start=start, end=end)
    except (IndexError, ValueError) as e:
        print(f"Usage: {sys.argv[0]} <integer> [start_integer] [end_integer]")
        print("Error:", e)

