class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            d = self.count(s)
            if d not in groups:
                groups[d] = [s]
            else:
                groups[d].append(s)

        return list(groups.values())

    @staticmethod
    def count(s: str) -> tuple[tuple[str]]:
        d = [0] * 26
        for el in s:
            idx = ord(el) - 97    
            d[idx] += 1
        return tuple(d)
