class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:

            if op == "+":
                a = stack.pop()
                b = stack[-1]
                stack.append(a)
                stack.append(a+b)
            elif op == "D":
                a = stack[-1] * 2
                stack.append(a)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        sum = 0
        for num in stack:
            sum += int(num)

        return sum