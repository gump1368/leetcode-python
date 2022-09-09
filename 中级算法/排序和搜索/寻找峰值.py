#！ -*- coding: utf-8 -*-
"""
@Author: gump
@Create Time: 20220905
@Info: 峰值元素是指其值严格大于左右相邻值的元素。
"""


def findPeakElement(nums):
    """
    输入：nums = [1,2,1,3,5,6,4]
    输出：1 或 5
    解释：你的函数可以返回索引 1，其峰值元素为 2；
        或者返回索引 5， 其峰值元素为 6。
    :param nums:
    :return:
    """
    # 二分法
    def bin_search(low, high):
        mid = (low + high) // 2
        if low < high:
            if nums[mid] > nums[mid+1]:
                return bin_search(low, mid)
            else:
                return bin_search(mid+1, high)
        return mid

    return bin_search(0, len(nums)-1)


if __name__ == '__main__':
    test_input = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(test_input))
