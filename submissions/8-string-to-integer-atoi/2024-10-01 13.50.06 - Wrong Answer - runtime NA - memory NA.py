class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        a = ""
        neg = False
        int_started = False
        i=0
        while i < len(s):
            if not s[i].isdigit() and s[i] not in [" ", "-", "+"]:
                break
            if (int_started and not s[i].isdigit()):
                break
            if not int_started and s[i].isdigit():
                int_started = True
                a += s[i]
            elif s[i].isdigit():
                a += s[i]
            if s[i] == " ":
                i+=1
                continue
            if s[i] == "-":
                neg = True
            
            i+= 1
        
        if a:
            ans = int(a)

        if neg:
            ans = ans* -1

        if ans > 2**31 -1:
            return 2**31 -1
        elif ans < -2**31:
            return -2**31
        return ans
