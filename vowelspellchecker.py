class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        
        vowels = "aeiou"

        def devowel(word: str) -> str:
            return "".join("*" if ch in vowels else ch for ch in word.lower())

        words = set(wordlist)
        lower_map = {}
        devowel_map = {}


        for word in wordlist:
            lowered = word.lower()
            vw = devowel(word)
            if lowered not in lower_map:
                lower_map[lowered] = word
            if vw not in devowel_map:
                devowel_map[vw] = word

        res = []
        for q in queries:
            if q in words:
                res.append(q)
            elif q.lower() in lower_map:
                res.append(lower_map[q.lower()])
            elif devowel(q) in devowel_map:
                res.append(devowel_map[devowel(q)])
            else:
                res.append("")
        return res
        
