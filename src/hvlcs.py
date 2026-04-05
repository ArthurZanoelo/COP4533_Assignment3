"""
Find the common subsequence of two strings
that maximizes the total character value.
"""

import sys


def parse_input(text: str) -> tuple[dict, str, str]:
    """
    Parse input format:
        K
        x1 v1
        x2 v2
        ...
        xK vK
        A
        B
    Returns (values dict, string A, string B)
    """
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    idx = 0

    k = int(lines[idx])
    idx += 1
    values = {}
    for _ in range(k):
        parts = lines[idx].split()
        idx += 1
        char, val = parts[0], int(parts[1])
        values[char] = val

    A = lines[idx]
    idx += 1
    B = lines[idx]
    idx += 1

    return values, A, B
