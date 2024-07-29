import math

def proper_fractions(d: int) -> int:
    if d == 1:
        return 0

    result = d
    limit = math.isqrt(d)

    for p in range(2, limit + 1):
        if d % p == 0:
            while (d := d // p) % p == 0:
                pass

            result -= result // p

    if d > 1:
        result -= result // d

    return result

# Not the best solution, but it works.
