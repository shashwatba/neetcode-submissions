class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMappings = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char not in bracketMappings:
                stack.append(char)
            else:
                if stack:
                    a = stack.pop()
                else:
                    return False
                if a != bracketMappings[char]:
                    return False

        if stack:
            return False
        else:
            return True
