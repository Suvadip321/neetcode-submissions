class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                currNum = num
                currLen = 1
                while currNum + 1 in nums_set:
                    currLen += 1
                    currNum += 1
                maxLen = max(maxLen, currLen)
        return maxLen
            
            