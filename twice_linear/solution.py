from typing import List
import heapq

def dbl_linear(n: int) -> int:
    if n == 0:
        return 1

    heap: List[int] = [1]
    seen: set[int] = {1}

    for _ in range(n):
        current = heapq.heappop(heap)

        for next_elem in (2 * current + 1, 3 * current + 1):
            if next_elem not in seen:
                seen.add(next_elem)
                heapq.heappush(heap, next_elem)

    # The smallest element in the heap is the (n+1)-th element in the sequence.
    return heapq.heappop(heap)
