from typing import List

def count_subsequences(needle: str, haystack: str) -> int:
    MOD = 10**8
    n, m = len(needle), len(haystack)

    dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0] = [1] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = (
              dp[i - 1][j - 1] 
              if needle[i - 1] == haystack[j - 1] 
              else 0
            ) + dp[i][j - 1]
            dp[i][j] %= MOD
            
    return dp[n][m]
