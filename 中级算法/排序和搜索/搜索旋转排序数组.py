#！ -*- coding: utf-8 -*-
"""
@Author: GUANDONGPU475
@Create Time: 20220909
@Info: 整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ...,
 nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为
  [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 
"""

def search(nums, target):
    if not nums:
        return -1

    num_k = nums[0]
    if num_k == target:
        return 0
    elif num_k < target:
        for i, num in enumerate(nums):
            if num < num_k:
                break
            elif num == target:
                return i
    elif num_k > target:
        for j in range(len(nums)-1, 0, -1):
            if nums[j]> num_k:
                break
            elif nums[j] == target:
                return j
    return -1


if __name__ == '__main__':
    test_input = [4,5,6,7,0,1,2]
    print(search(test_input, 0))
