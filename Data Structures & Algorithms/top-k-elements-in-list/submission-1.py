class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for x in nums:
            freq[x]=freq.get(x, 0)+1
        values=list(freq.keys())
        values.sort(key=lambda x: freq[x], reverse=True)
        return values[:k]
        