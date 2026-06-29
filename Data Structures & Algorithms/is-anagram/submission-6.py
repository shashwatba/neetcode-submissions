class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {}
        lettersT = {}
        if len(t) < len(s) or len(t) > len(s):
            return False
        for char in s:
            if char not in lettersS:
                lettersS[char] = 1
            else:
                lettersS[char] += 1
        for char in t:
            if char not in lettersS:
                return False
            elif char not in lettersT:
                lettersT[char] = 1
            else:
                lettersT[char] +=1

        for char in t:
            if lettersS[char] != lettersT[char]:
                return False
            
        return True