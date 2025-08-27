class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i.strip("-").isdigit():
                res.append(int(i))
            elif i == '+':
                if len(res) >= 2:
                    res.append(res[len(res) - 1] + res[len(res) - 2])
                elif len(res) == 1:
                    res.append(res[0])
                else:
                    res.append(0)
            elif i == 'D':
                if len(res) >= 1:
                    res.append(res[len(res) - 1] * 2)
                else:
                    res.append(0)
            elif i == 'C':
                if res:
                    res.pop()
        return sum(res)
