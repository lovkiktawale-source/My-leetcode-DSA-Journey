class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        # An IP address cannot have more than 12 digits or fewer than 4 digits
        if len(s) < 4 or len(s) > 12:
            return res

        def backtrack(start: int, dots: int, current_ip: str):
            # Base case: 4 segments placed
            if dots == 4:
                if start == len(s):
                    res.append(current_ip[:-1])  # remove trailing dot
                return

            # Explore segment lengths from 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start : start + length]
                
                # Check for leading zero rule and valid integer range [0, 255]
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(start + length, dots + 1, current_ip + segment + ".")

        backtrack(0, 0, "")
        return res