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


def hvlcs(A: str, B: str, values: dict) -> tuple[int, str]:
    """
    Compute the Highest Value Common Subsequence of A and B.

    Let OPT[i][j] = max value of a common subsequence of A[0..i-1] and B[0..j-1].

    Base cases:
        OPT[0][j] = 0  for all j  (empty prefix of A -> no common characters)
        OPT[i][0] = 0  for all i  (empty prefix of B -> no common characters)

    Recurrence:
        If A[i-1] == B[j-1]:
            OPT[i][j] = OPT[i-1][j-1] + v(A[i-1])
                (we can always extend a common subsequence by matching equal chars,
                matching is never worse than skipping)
        Else:
            OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1])
                (skip either A[i-1] or B[j-1] and just take the better option)

    Reasoning:
        - When characters match, including them never decreases value (v >= 0), so we
          always take the match.
        - When they differ, the optimal subsequence either excludes A[i-1] or B[j-1],
          so we take the max of both sub-problems.
        - The table is filled in order of increasing i and j, so all sub-problems are
          solved before they are needed.

    Runtime is O(n * m), where n = size of A and m = size of B.
    """
    n, m = len(A), len(B)

    # Build DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return dp[n][m], "".join(result)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    values, A, B = parse_input(text)
    max_val, subseq = hvlcs(A, B, values)

    print(max_val)
    print(subseq)


if __name__ == "__main__":
    main()