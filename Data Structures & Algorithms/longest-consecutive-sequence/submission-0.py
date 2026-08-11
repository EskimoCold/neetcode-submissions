class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_seq = 0
        for n in nums:
            if n - 1 not in nums_set:
                k = n
                current_seq = 0
                while k in nums_set:
                    k += 1
                    current_seq += 1
                longest_seq = max(longest_seq, current_seq)

        return longest_seq
