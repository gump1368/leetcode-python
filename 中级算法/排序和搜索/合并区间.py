#！ -*- coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20220908
@Info: 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，
并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""


def merge(intervals):
    """
    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    :param intervals:
    :return:
    """
    def merge_two(interval1, interval2):
        result = []
        while interval1 and interval2:
            if interval1[0][0] < interval2[0][0]:
                result.append(interval1.pop(0))
            else:
                result.append(interval2.pop(0))
        while interval1:
            result.append(interval1.pop(0))
        while interval2:
            result.append(interval2.pop(0))

        for i, res in enumerate(result):
            while i+1 < len(result):
                next_res = result[i+1]
                if next_res[0] > res[1]:
                    break
                else:
                    result[i] = [res[0], max(res[1], next_res[1])]
                    result.pop(i+1)
                    res = result[i]
        return result

    def merge_sort(arrs):
        if len(arrs) < 2:
            return arrs
        mid = len(arrs) // 2
        left, right = arrs[0:mid], arrs[mid:]
        return merge_two(merge_sort(left), merge_sort(right))
    return merge_sort(intervals)


if __name__ == '__main__':
    test_input = [[1,4],[1,5]]
    print(merge(test_input))