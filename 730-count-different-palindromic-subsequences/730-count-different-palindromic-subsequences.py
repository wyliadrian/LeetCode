class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
        for distance in range(1, l):
            for i in range(l - distance):
                j = i + distance
                if s[i] == s[j]:
                    low = i + 1
                    high = j - 1
                    while low <= high and s[low] != s[j]:
                        low += 1
                    while low <= high and s[i] != s[high]:
                        high -= 1
                    if low > high:
                        dp[i][j] = dp[i+1][j-1]*2 + 2
                    elif low == high:
                        dp[i][j] = dp[i+1][j-1]*2 + 1
                    else:
                        dp[i][j] = dp[i+1][j-1]*2 - dp[low+1][high-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
        return dp[0][-1] % (10**9 + 7)