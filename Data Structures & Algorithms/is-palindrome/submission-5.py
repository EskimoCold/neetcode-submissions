class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = [el.lower() for el in s if el.isalnum()]
        return modified == modified[::-1]
