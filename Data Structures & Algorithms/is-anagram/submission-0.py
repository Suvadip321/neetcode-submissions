class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1
        return freq_s == freq_t
