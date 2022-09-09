# ！ -*- coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20220819
@Info:
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。
"""

def sort_colors(nums: list):
    """
    输入：nums = [2,0,2,1,1,0]
    输出：[0,0,1,1,2,2]
    :param nums:
    :return:
    """
    if not nums:
        return nums

    for i, num in enumerate(nums):
        last_num = nums[i-1] if i-1 >= 0 else num
        while num < last_num:
            nums[i] = last_num
            nums[i-1] = num
            num = nums[i-1]
            i -= 1
            if i <= 0:
                break
            last_num = nums[i-1]
    return nums


if __name__ == '__main__':
    test_nums = [2, 0, 1]
    print(sort_colors(test_nums))
