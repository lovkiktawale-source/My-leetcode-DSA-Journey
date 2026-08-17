class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer if current character is not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer if current character is not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters after converting to lowercase
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True