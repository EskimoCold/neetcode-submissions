class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for el in s:
            counter[el] = counter.get(el, 0) + 1

        for el in t:
            if el in counter:
                counter[el] -= 1
            else:
                return False

        for value in counter.values():
            if value != 0:
                return False

        return True
