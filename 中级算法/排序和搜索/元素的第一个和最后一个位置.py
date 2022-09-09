#！ -*- coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20220907
@Info: 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
"""

def searchRange(nums, target):
    """
    输入：nums = [5,7,7,8,8,10], target = 8
    输出：[3,4]
    :param nums:
    :param target:
    :return:
    """
    def bin_search(low, high):
        mid = (low + high) // 2
        if low < high:
            if nums[mid] < target:
                return bin_search(mid+1, high)
            elif nums[mid] > target:
                return bin_search(low, mid-1)
            else:
                return mid
        elif nums[mid] == target:
            return mid
        return -1

    position = bin_search(0, len(nums)-1)
    if position == -1:
        return [-1, -1]

    left, right = position, position

    while left >= 0 and nums[left] == target:
        left -= 1
    while right < len(nums) and nums[right] == target:
        right += 1

    return [left+1, right-1]


if __name__ == '__main__':
    test_input = [1]
    print(searchRange(test_input, 1))



