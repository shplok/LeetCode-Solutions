class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # n = num languages
        # languages[i] = languages user at i knows
        # friendships[i] = friends of user 1 at i and user 2 at i

        cant = set()
        for f in friendships:
            mp = {}
            con = False
            for lang in languages[f[0] - 1]:
                mp[lang] = 1
            for lang in languages[f[1] - 1]:
                if lang in mp:
                    con = True
                    break
            if not con:
                cant.add(f[0] - 1)
                cant.add(f[1] - 1)

        max_cnt = 0
        cnt = [0] * (n + 1)
        for f in cant:
            for lang in languages[f]:
                cnt[lang] += 1
                max_cnt = max(max_cnt, cnt[lang])

        return len(cant) - max_cnt
