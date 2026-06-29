class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tracker = {}
        for char in s:
            if char in tracker:
                tracker[char] += 1
            else:
                tracker[char] = 1
        
        for c in t:
            if c not in tracker or tracker[c] == 0:
                return False
            tracker[c] -= 1

        return True
        