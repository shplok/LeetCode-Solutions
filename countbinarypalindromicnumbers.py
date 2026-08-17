class Solution:
    def countBinaryPalindromes(self, n: int) -> int:

        if n == 0:
            return 1

        binN = bin(n)[2:]
        l = len(binN)
        cnt = 1

        for length in range(1, l):
            half = (length + 1) //2
            cnt += 1 << (half - 1)

        half = (l + 1 ) // 2
        pref = int(binN[:half], 2)

        cnt += pref - (1 << (half - 1))

        prefBin = bin(pref)[2:]

        if len(prefBin) < half:
            prefBin = "0" * (half - len(prefBin))


        if l % 2 == 0:
            palBin = prefBin + prefBin[::-1]
        else:
            palBin = prefBin + prefBin[-2::-1]
        pal = int(palBin, 2)
        if pal <= n:
            cnt += 1

        return cnt
