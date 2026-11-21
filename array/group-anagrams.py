# Pattern: sort words alphabetically & use as key
# Time: O(n * klogk) (sorting word costs klogk)
# Space: O(nk) (store every word's characters)
# Mistakes: how to save actual words
# Revisit: yes

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Inputs: list of strings
        # Outputs: list of list of strings, grouped by anagrams

        groups = {}

        for word in strs:
            # Sort word alphabetically
            key = ''.join(sorted(word))
            # Init list if new key
            if key not in groups:
                groups[key] = []
            # Add word to list
            groups[key].append(word)
        
        return list(groups.values())