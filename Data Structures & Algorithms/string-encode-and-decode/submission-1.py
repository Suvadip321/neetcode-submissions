class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

        # decoded = []
        # i = 0
        # while i < (len(s)):
        #     j = i
        #     while s[j] != "#":
        #         j += 1
        #     n = int(s[i:j])
        #     j += 1
        #     decoded.append(s[j:j+n])
        #     i = j + n
        # return decoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            n = int(s[i:j])
            j += 1
            i = j + n
            decoded.append(s[j:i])
        return decoded

        


