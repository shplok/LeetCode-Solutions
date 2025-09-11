class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        currVowels = []
        cnt = 0
        res = []
        for char in s:
            if char in vowels:
                currVowels.append(char)

        currVowels.sort()
        
        for char in s:
            if char in vowels:
                res.append(currVowels[cnt])
                cnt += 1
            else:
                res.append(char)
        return ''.join(res)
