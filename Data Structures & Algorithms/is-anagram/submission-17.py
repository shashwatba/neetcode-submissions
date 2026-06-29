class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_of_chars = {}
        for char in s:
            if char in map_of_chars:
                map_of_chars[char] += 1
            else:
                map_of_chars[char] = 1
        
        for new_char in t:
            if new_char not in map_of_chars:
                return False
            else:
                map_of_chars[new_char] -= 1

        for char in s:
            if map_of_chars[char] != 0:
                return False

        return True
        