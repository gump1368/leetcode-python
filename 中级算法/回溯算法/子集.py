# ！-*-coding: utf-8-*-
"""
@Author: GUMP
@Create Time: 20220707
@Info: 子集
"""


def subsets(nums):
    """
    输入：nums = [1,2,3]
    输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    :param nums:
    :return:
    """
    result = [[]]

    def trace_back(new_nums):
        if new_nums in result:
            return

        result.append(new_nums)
        for i in range(len(new_nums)):
            other = new_nums[:i] + new_nums[i+1:]
            trace_back(other)
            # result.remove(new_nums)
            # new_nums
            # new_nums
            # if num not in result:
            #     result.append(num)
            # if other not in result:
            #     result.append(other)
            #
            # trace_back(other)

    trace_back(nums)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(subsets(nums))
    # print(sorted(subsets(nums), key=lambda x: len(x)))