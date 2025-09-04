def lower_bound1(nums: List[int], target: int) -> int:
    #tc O(log n)
    #sc O(1)
    left = 0
    right = len(nums) - 1  # 闭区间 [left,right]
    while left <= right:  # 区间不为空
        mid = left + (right - left)//2
        if nums[mid] < target:
            left = mid + 1  #[mid+1,right]
        else: 
            right = mid - 1 #[left, mid-1]
    return left

def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left,right)
    while left < right:  # 区间不为空
        mid = left + (right - left)//2
        if nums[mid] < target:
            left = mid + 1  #[mid+1,right)
        else:
            right = mid #[left, mid)
    return left # right

def lower_bound3(nums: List[int], target: int) -> int:
    left = -1
    right = len(nums) - 1  # 开区间 (left,right)
    while left + 1 < right:  # 区间不为空
        mid = left + (right - left)//2
        if nums[mid] < target:
            left = mid  #(mid, right)
        else:
            right = mid #(left, mid)
    return right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound1(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1 , -1]
        end = lower_bound1(nums, target + 1) - 1
        return [start, end]