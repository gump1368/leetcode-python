# ！ -*-coding: utf-8 -*-
"""
@Author: GUANDONGPU475
@Create Time: 20220826
@Info:
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
"""


def findKthLargest(nums, k):
    """
    :param nums: [3,2,3,1,2,4,5,5,6]
    :param k: 4
    :return: 4
    """
    def build_max_heap(i, end):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left < end and nums[i] < nums[left]:
            largest = left
        if right < end and nums[i] < nums[right] and nums[left] < nums[right]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            build_max_heap(largest, end)

    # 调整最大堆
    for j in range((len(nums)-2)//2, -1, -1):
        build_max_heap(j, len(nums))

    # 堆排序
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        build_max_heap(0, j-1)

    return nums[-k]


if __name__ == '__main__':
    test_input = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    test_k = 4
    print(findKthLargest(test_input, test_k))
