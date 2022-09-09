# ！ -*- coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20220824
@Info:
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
"""
import collections


# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
def topKFrequent(nums, k):
    count = collections.Counter(nums)
    res = sorted(count.items(), key=lambda x: x[1], reverse=True)

    return [value[0] for value in res][:k]


if __name__ == '__main__':
    test_input = [1, 1, 1, 2, 2, 3]
    test_k = 2
    print(topKFrequent(test_input, test_k))
