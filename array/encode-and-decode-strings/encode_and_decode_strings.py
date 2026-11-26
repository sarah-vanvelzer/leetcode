# Pattern: track new strings via length count + symbol to break up length from actual string
# Time:
#   encode: O(n*m) where n is the number of strings & m is the string length
#   decode: O(n^2*m) (since recopied into the list within loop)
# Space:
#   encode: O(n*m)
#   decode: O(n*m)
# Mistakes: understanding what to do + syntax
#   need to use index instead of slicing (next time!!)
# Revisit: yes

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Inputs: a list of strings
        # Outputs: a single decodable string

        encoding = ""

        for i in range(len(strs)):
            curr_length = len(strs[i])
            encoding = encoding + str(curr_length) + "#"
            encoding += strs[i]
        
        return encoding

    def decode(self, s: str) -> List[str]:
        # Inputs: a single decodable string
        # Outputs: a list of strings

        decoded = []
        
        while s:
            j = 0
            len_str = ""
            while s[j] != '#':
                len_str += s[j]
                j += 1
            word_len = int(len_str)
            # skip '#'
            s = s[j + 1:]

            curr_word = ""
            for i in range(word_len):
                curr_word += s[i]

            decoded.append(curr_word)
            s = s[word_len:]

        return decoded            
