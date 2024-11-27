class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # i represents the paper (ith paper)
        # citations[i] represents the number of citations they got for the paper
        # h-index = max value of h such that the researcher published h papers 
        # with h # citations
        # h-index (f) = max{i∈N:f(i) >= i}

        n = len(citations)
        citations.sort()
        
        for i, paper in enumerate(citations):
            h = n - i
            if h <= paper:
                return h
        return 0
