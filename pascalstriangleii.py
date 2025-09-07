class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 1 - 0
        # 1 1 - 1
        # 1 2 1 - 2
        # 1 3 3 1 - 3
        # 1 4 6 4 1 - 4

        res = [1]
        if rowIndex <= 0:
            return res
        elif rowIndex == 1:
            res.append(1)
            return res

        for i in range(1, rowIndex + 1):
            curr = [1]
            if (i == 1):
                curr.append(1)
            else:
                for j in range(1, i + 1):
                    calc = 1
                    if j == i:
                        curr.append(1)
                    else:
                        prev = res[i-1]
                        calc = prev[j-1] + prev[j]
                        curr.append(calc)
            res.append(curr)
        return res[-1]
