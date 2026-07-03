class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s.lower():
            if char.isalnum():
                new_str += char

        left_p = 0
        right_p = len(new_str) - 1

        while left_p < right_p:
            if new_str[left_p] == new_str[right_p]:
                left_p += 1
                right_p -= 1
            else:
                return False
        
        return True
