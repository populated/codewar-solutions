from typing import List

def solution(args: List[int]) -> str:
    assert all(x < y for x, y in zip(args, args[1:])), "Input list must be sorted in increasing order"

    def format_range(start: int, end: int) -> str:
        return (
            f"{start}-{end}"
            if end - start > 1
            else ",".join(map(str, range(start, end + 1)))
        ) # How boring.

    ranges = []
    start = args[0]

    for i in range(1, len(args)):
        # If the current element is not equal to the previous element plus one,
        # then we have reached the end of a range.
        if args[i] != args[i-1] + 1:
            ranges.append(format_range(start, args[i-1]))
            start = args[i]

    ranges.append(format_range(start, args[-1]))

    return ",".join(ranges)
