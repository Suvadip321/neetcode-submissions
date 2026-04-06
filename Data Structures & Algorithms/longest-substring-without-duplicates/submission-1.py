class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        last_seen = {}
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1
            last_seen[ch] = r
            maxlen = max(maxlen, r - l + 1)
        return maxlen