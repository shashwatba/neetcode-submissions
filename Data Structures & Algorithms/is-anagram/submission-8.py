class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in smap:
                smap[char] = smap[char] + 1
            else:
                smap[char] = 1
        for tchar in t:
            if tchar in smap:
                if smap[tchar] == 0:
                    return False
                smap[tchar] = smap[tchar] - 1
            else:
                return False
        return True
