class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_of_s = {}
        
        for char in s:
            if char not in map_of_s:
                map_of_s[char] = 1
            else:
                map_of_s[char] += 1
        
        for char in t:
            if char not in map_of_s or map_of_s[char] == 0:
                return False
            map_of_s[char] -= 1

        return True

        