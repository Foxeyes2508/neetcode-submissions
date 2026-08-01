class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        for i in range(len(s)):
            temp = expand(i, i)
            if len(temp) > res_len:
                res = temp
                res_len = len(temp)
            temp = expand(i, i+1)
            if len(temp) > res_len:
                res = temp
                res_len = len(temp)

        return res