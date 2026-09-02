class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]   # worst case: cut before every char

        for center in range(n):
            # odd length palindromes
            l, r = center, center
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r] = min(dp[r], (dp[l - 1] + 1) if l > 0 else 0)
                l -= 1
                r += 1

            # even length palindromes
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r] = min(dp[r], (dp[l - 1] + 1) if l > 0 else 0)
                l -= 1
                r += 1

        return dp[n - 1]