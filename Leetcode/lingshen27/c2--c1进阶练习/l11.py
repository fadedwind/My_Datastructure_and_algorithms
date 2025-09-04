class Solution:
    def maxArea(self, height: List[int]) -> int:
        #两侧指针合起来只遍历这个数组一次，O(n)
        #空间复杂度：O(1)
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left)*min(height[left],height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans