class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)

            hashmap[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len