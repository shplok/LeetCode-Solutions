def merge(l, r):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res.extend(l[i:])
    res.extend(r[j:])
    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])

    return merge(l, r)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)
