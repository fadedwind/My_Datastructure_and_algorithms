
class Solution:

    ##暴力
    def minSubArrayLen0(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')          

        for l in range(n):
            cur_sum = 0                
            for r in range(l, n):
                cur_sum += nums[r]
                if cur_sum >= target:   
                    min_len = min(min_len, r - l + 1)
                    break               
        return min_len if min_len != float('inf') else 0
    
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        # tc: o(n)
        # sc: o(1)
        n = len(nums)
        ans = inf       

        s = 0
        left = 0

        for right, x in enumerate(nums): # x:nums[right] right:(0,n) -->> 0 ~ n-1
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right-left+1) #假设l=r 这时窗口子数组大小为1，所以这里有个+1
        return ans if ans <= n else 0
