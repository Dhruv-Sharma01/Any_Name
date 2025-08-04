"""A simple module to demonstrate a clean Python script for Pylint."""

import math


def compare_values(x: int, y: int) -> str:
    """Compares two integers and returns a message."""
    if x > y:
        return "x is greater"
    elif y > x:
        return "y is greater"
    return "equal"


def process_values() -> int:
    """Processes a loop with conditional branching."""
    for i in range(10):
        if i % 2 == 0:
            continue
        else:
            break
    return i


def safe_input(prompt: str) -> str:
    """Safely gets input from the user (stub)."""
    return prompt  # Placeholder for real input()


def increment(x: int) -> int:
    """Returns x incremented by 1."""
    return x + 1


if __name__ == "__main__":
    result = compare_values(5, 3)
    print(result)
    print(process_values())
