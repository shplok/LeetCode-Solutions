class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        comp = ''
        for i in b:
            if i == '1':
                comp += '0'
            else:
                comp += '1'

        return int(comp, 2)
        