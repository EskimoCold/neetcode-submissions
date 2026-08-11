class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for n, count in counter.items():
            freq[count].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
