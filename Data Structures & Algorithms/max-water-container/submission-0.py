class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        lheight, rheight = 0,0
        maxarea = 0
        while l < r:
            lheight = max(lheight,heights[l])
            rheight = max(rheight,heights[r])
            
            minheight = min(lheight,rheight)

            area = (r - l) * (minheight)
            maxarea = max(area,maxarea)

            if lheight > minheight:
                r -= 1
            elif rheight > minheight:
                l += 1

            else:
                l += 1
                r -= 1

        return maxarea

