class Solution:
    def generate_strings(self, s, t, n, out):
        if t == n:
            out.append(s)
            return
        if not s:
            self.generate_strings(s+"0", t+1, n, out)
            self.generate_strings(s+"1", t+1, n, out)
        elif s[t-1] == '0':
            self.generate_strings(s+"1", t+1, n, out)
        else:
            self.generate_strings(s+"0", t+1, n, out)
            self.generate_strings(s+"1", t+1, n, out)            
        return out

    def validStrings(self, n: int) -> List[str]:
        out = []
        return self.generate_strings("", 0, n, out)
        