class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while True: #left < right
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s > target:
                right -= 1 # cut off the rightest number
            if s < target:
                left += 1
        return [left + 1, right + 1]
    

    # 1 2 3 4 5