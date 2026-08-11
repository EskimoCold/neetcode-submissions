class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        sorted_keys = sorted(counter.keys(), key=counter.get, reverse=True)
        return sorted_keys[:k]
