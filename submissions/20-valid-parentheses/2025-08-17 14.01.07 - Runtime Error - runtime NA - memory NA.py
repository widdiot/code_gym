class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clos = set(['}',']',')'])
        hmap = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if i not in clos:
                stack.append(i)
            else:
                if stack[-1] == hmap[i]:
                    stack.pop()
                else:
                    return False
        return not stack

        