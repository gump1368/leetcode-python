#！ -*- coding: utf-8 -*-
"""
@Author: GUMP
@Create Time: 20220915
@Info: 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
"""

def canJump(nums):
    """
    输入：nums = [2,3,1,1,4]
    输出：true
    :param nums:
    :return:
    """
    if not nums:
        return False
    target = len(nums)-1

    def temp(value):
        if value == target:
            return True
        num = nums[value]
        for i in range(1, num+1):
            total = value + i
            if total < target:
                res = temp(total)
                if res:
                    return True
            elif total == target:
                return True
            else:
                break
        return False

    return temp(0)


def canJump1(nums):
    """
    输入：nums = [2,3,1,1,4]
    输出：true
    :param nums:
    :return:
    """
    if not nums:
        return False
    if nums[0] >= len(nums)-1:
        return True
    if nums[0] == 0:
        return False
    temp = [nums[0]]
    for i in range(1, len(nums)):
        temp.append(max(temp[i-1]-1, nums[i]))
        if temp[i] + i >= len(nums)-1:
            return True
        elif temp[i] == 0:
            return False
    return False

if __name__ == '__main__':
    test_input = [0,1]
    print(canJump1(test_input))
