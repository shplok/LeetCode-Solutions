class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1] * len(rains)
        st = SortedList()
        mp = {}

        for i, rain in enumerate(rains):
            if rain == 0:
                st.add(i)
            else:
                res[i] = -1
                if rain in mp:
                    bi = st.bisect(mp[rain])
                    if bi == len(st):
                        return []
                    res[st[bi]] = rain
                    st.discard(st[bi])
                mp[rain] = i
        return res
