class Solution:
    def isValid(self, s: str) -> bool:

        mapOfChars = {"(":")", "[":"]", "{":"}"}

        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if mapOfChars[a] != char:
                    return False



        if len(stack) != 0:
            return False

        return True