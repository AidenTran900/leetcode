class Solution:
    def isValid(self, s: str) -> bool:
        CLOSE_PAIR = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        stack = []
        for char in s:
            if stack and stack[-1] in CLOSE_PAIR and char == CLOSE_PAIR[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0