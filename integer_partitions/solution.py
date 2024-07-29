from itertools import combinations_with_replacement
from typing import List, Set
from functools import reduce
import operator

def partitions(n: int) -> List[List[int]]:
    def _partitions(n: int, max_val: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        
        return [
            [i] + p
            for i in range(1, min(n, max_val) + 1)
            for p in _partitions(n - i, i)
        ]

    return _partitions(n, n)

def product(partition: List[int]) -> int:
    return reduce(operator.mul, partition, 1)

def prod(n: int) -> List[int]:
    return sorted(set(product(p) for p in partitions(n)))

def stats(products: List[int]) -> str:
    range_val = products[-1] - products[0]
    average = sum(products) / len(products)
    median = (
        products[len(products) // 2]
        if len(products) % 2 != 0
        else (products[len(products) // 2 - 1] + products[len(products) // 2]) / 2
    )
  
    return f"Range: {range_val} Average: {average:.2f} Median: {median:.2f}"

def part(n: int) -> str:
    products = prod(n)
    return stats(products)
