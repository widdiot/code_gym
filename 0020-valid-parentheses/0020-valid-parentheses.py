class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in hmap:
                stack.append(i)
            elif i in hmap.values():
                if len(stack) > 0:
                    if hmap[stack[-1]] != i:
                        return False
                    stack.pop()
                else:
                    return False
        return len(stack) == 0