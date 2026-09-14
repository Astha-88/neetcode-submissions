class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i,0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        ans = []

        for i in range(len(freq) - 1,0,-1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        return -1