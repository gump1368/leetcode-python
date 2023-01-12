#！ -*-coding: utf-8 -*-
"""
@author: gump
@create time: 20221208
@Info:
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""

def lengthOfLIS(nums):
    """
    输入：nums = [0,1,0,3,2,3]
    输出：4
    :param nums:
    :return:
    """
    length = len(nums)
    dp = [1] * length
    for i in range(length):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)




if __name__ == '__main__':
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))