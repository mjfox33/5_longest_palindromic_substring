class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return None
        n = len(s)
        if n == s.count(s[0]):
            return s
        if n == 3:
            if s[0] == s[2]:
                return s
            elif s[0] == s[1]:
                return s[0:2]
            elif s[1] == s[2]:
                return s[1:3]
            else:
                return s[0]

        max_length = 1
        max_start = 0

        dp = [ [0]*n for _ in range(n)]

        # dp init
        for i in range(n):
            # single length strings are always a palindrome
            dp[i][i] = 1

            # n=2 are palindrome if strings are equal
            if i < n-1:
                if s[i] == s[i+1]:
                    dp[i][i+1] = 1
                    max_start = i
                    max_length = 2
        

        for k in range(3,n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    max_start = i
                    max_length = k

        return s[max_start:max_start+max_length]
