# Pattern: use dictionary to store counts
# Time: O(n)
# Space: O(n)
# Mistakes: checking list adding complexity
# Revisit: no

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Inputs: strings s & t
        # Ouputs: true if t is an annagram of s

        # Key = character & value = count
        s_chars = {}

        for c in s:
            if c in s_chars:
                s_chars[c] = s_chars[c] + 1
            else:
                s_chars[c] = 1
        
        # Decrement dictionary when in t
        for c in t:
            if c in s_chars:
                s_chars[c] = s_chars[c] - 1
                # Remove key when count gets to 0
                if s_chars[c] == 0:
                    s_chars.pop(c)
            else:
                return False
        
        if s_chars == {}:
            return True
        else:
            return False