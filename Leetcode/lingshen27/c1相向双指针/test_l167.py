import pytest
from typing import List

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s > target:
                right -= 1
            if s < target:
                left += 1
        return [left + 1, right + 1]


def test_two_sum_basic_case():
    """测试基础用例：存在解且位于数组中间"""
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(numbers, target)
    assert result == [1, 2]


def test_two_sum_first_and_last():
    """测试首尾元素组合的情况"""
    sol = Solution()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 11
    result = sol.twoSum(numbers, target)
    assert result == [1, 10]


def test_two_sum_adjacent_elements():
    """测试相邻元素组合的情况"""
    sol = Solution()
    numbers = [1, 3, 4, 6, 8, 10]
    target = 7
    result = sol.twoSum(numbers, target)
    assert result == [2, 3]


def test_two_sum_negative_numbers():
    """测试包含负数的情况"""
    sol = Solution()
    numbers = [-5, -3, 0, 2, 4, 7]
    target = 1
    result = sol.twoSum(numbers, target)
    assert result == [2, 5]


def test_two_sum_duplicate_numbers():
    """测试包含重复数字的情况"""
    sol = Solution()
    numbers = [1, 2, 2, 3, 4, 5]
    target = 4
    result = sol.twoSum(numbers, target)
    assert result == [1, 4]


def test_two_sum_minimum_length():
    """测试最小长度数组的情况"""
    sol = Solution()
    numbers = [1, 2]
    target = 3
    result = sol.twoSum(numbers, target)
    assert result == [1, 2]


def test_two_sum_large_numbers():
    """测试大数字的情况"""
    sol = Solution()
    numbers = [1000, 2000, 3000, 4000, 5000]
    target = 7000
    result = sol.twoSum(numbers, target)
    assert result == [2, 5]


def test_two_sum_consecutive_numbers():
    """测试连续数字的情况"""
    sol = Solution()
    numbers = [10, 11, 12, 13, 14, 15]
    target = 25
    result = sol.twoSum(numbers, target)
    assert result == [3, 4]


def test_two_sum_zero_target():
    """测试目标值为0的情况"""
    sol = Solution()
    numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    target = 0
    result = sol.twoSum(numbers, target)
    assert result == [1, 9]


def test_two_sum_large_array():
    """测试较大数组的情况"""
    sol = Solution()
    numbers = list(range(1, 1001))
    target = 1999  # 1000 + 999
    result = sol.twoSum(numbers, target)
    assert result == [999, 1000]