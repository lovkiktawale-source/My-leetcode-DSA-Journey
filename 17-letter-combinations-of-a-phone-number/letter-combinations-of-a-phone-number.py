class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Base case: if the input is empty, return an empty list
        if not digits:
            return []
            
        # Mapping of digits to letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_combination):
            # If the combination is done
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get the letters that the current digit maps to
            next_digit = digits[index]
            for letter in phone_map[next_digit]:
                # Add the letter to the current combination
                current_combination.append(letter)
                # Move on to the next digit
                backtrack(index + 1, current_combination)
                # Backtrack by removing the letter before trying the next one
                current_combination.pop()
        
        # Initiate the backtracking from the first digit
        backtrack(0, [])
        return result