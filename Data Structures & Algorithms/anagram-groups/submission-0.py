from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for char in s:
                letters[ord(char) - ord('a')] += 1
            map[tuple(letters)].append(s)

        return map.values()