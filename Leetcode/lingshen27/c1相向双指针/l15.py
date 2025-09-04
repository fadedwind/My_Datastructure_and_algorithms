class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()   # o(nlogn)
    # 三元组的顺序并不重要
    # ->   i < j < k
    # 答案中不可包含重复的三元组

        ans = []
        n = len(nums)
        for i in range(n-2): #(n-2,n-1 留给 jk---->  i 枚举到n-3， range大小就是n-2)      
        # 时间复杂度O(n平方)，里外各一层O(n)
        # 空间复杂度由于没有用额外变量所以是O(1)
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            # 小优化1
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[n-2] + nums[n-1] < 0:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])

                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return ans