class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        firstStringMap = {}
        secondStringMap = {}
        for char in s:
            if char in firstStringMap:
                firstStringMap[char] += 1
            else:
                firstStringMap[char] = 1
        
        for char in t:
            if char in secondStringMap:
                secondStringMap[char] += 1
            else:
                secondStringMap[char] = 1

        for char in s:
            if char not in secondStringMap:
                return False
            if firstStringMap[char] != secondStringMap[char]:
                return False

        return True
        