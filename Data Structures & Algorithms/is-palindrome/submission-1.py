class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = "".join([el.lower() for el in s if el.isalpha() or el.isdigit()])
        return modified == modified[::-1]
