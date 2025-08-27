class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        a = ""
        neg = False
        int_started = False
        valid_chars = set(["0","1","2","3","4","5","6","7","8","9"," ","+","-"])
        i=0
        while i < len(s):
            if s[i] not in valid_chars:
                break
            if int_started:
                if s[i].isdigit():
                    a += s[i]
                else:
                    break
            if not int_started and (s[i].isdigit() or s[i] in ["-", "+"]):
                int_started = True
                if s[i].isdigit():
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
