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


def format_change(change: list[int]) -> str:
    """Format the change nicely"""
    if len(change) != 4:
        raise ValueError("Invalid change")
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
        if amount < 0:
            raise ValueError("Invalid amount")
        output += f"{amount} {coin[int(amount == 1)]}\n"
    return output


if __name__ == "__main__":
    print(
        format_change(
            get_exact_change(int(input("Enter the amount of change in cents: ")))
        )
    )
