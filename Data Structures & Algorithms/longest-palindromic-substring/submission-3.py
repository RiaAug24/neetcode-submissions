class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        res = ""
        resLen = 0
        for i in range(n):
            # Odd Palindrome check

            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1

            # Even Palindrome check

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
        return res

                
        

        