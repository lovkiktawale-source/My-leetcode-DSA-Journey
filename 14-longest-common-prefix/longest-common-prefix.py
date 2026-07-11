class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Take the first string as a reference
        first_str = strs[0]
        
        for i in range(len(first_str)):
            char = first_str[i]
            # Check this character against all other strings
            for other_str in strs[1:]:
                # If the current string is shorter or the character doesn't match
                if i == len(other_str) or other_str[i] != char:
                    return first_str[:i]
                    
        return first_str