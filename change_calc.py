#!/usr/bin/env python3
"""Given an amount of change in cents, return the amount of each coin you have"""


def get_exact_change(cents: int) -> list[int]:
    """
    Compute the actual math: going from most to least,
    add each coin amount to a change list.

    Return the change list
    """
    change = [cents, 0, 0, 0]
    for i, j in enumerate((25, 10, 5)):
        change[i], change[i + 1] = divmod(change[i], j)
    return change


def print_change(change: list[int]) -> None:
    """Format the change nicely and print it"""
    if len(change) != 4:
        print("Invalid change")
        return
    output = ""
    for amount, coin in zip(
        change,
        (
            ("quarters", "quarter"),
            ("dimes", "dime"),
            ("nickels", "nickel"),
            ("pennies", "penny"),
        ),
    ):
        if amount == 1:
            output += f"{amount} {coin[1]}\n"
        elif amount > 1:
            output += f"{amount} {coin[0]}\n"
        elif amount == 0:
            continue
    print(output)


if __name__ == "__main__":
    print_change(get_exact_change(int(input("Enter the amount of change in cents: "))))
