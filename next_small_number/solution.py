from typing import List

def next_smaller(n: int) -> int:
    assert n > 0, "Input must be a positive integer"

    digits: List[int] = [int(d) for d in str(n)]
    for i in reversed(range(len(digits) - 1)):
        if digits[i] > digits[i + 1]:
            break
    else:
        return -1

    for j in reversed(range(i + 1, len(digits))):
        if digits[j] < digits[i]:
            break

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)
    result: int = int(''.join(str(d) for d in digits))
    
    # If the result has a leading zero, return -1
    
    return result if result >= 10 ** (len(digits) - 1) else -1
