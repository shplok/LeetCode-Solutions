class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = ''

        for word in words:
            if sorted(word) != sorted(prev):
                res.append(word)
                prev = word

        return res
