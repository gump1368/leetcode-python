"""
输入: [1,2,3,4,5]
输出: true
"""


def increasingTriplet(nums):
    res = [[nums[0]]]

    for num in nums[1:]:
        if num < res[-1][0]:
            res.append([num])
        else:
            for item in res:
                if num > item[-1]:
                    item.append(num)
                elif len(item) == 2 and item[0] < num:
                    item[1] = num

                if len(item) == 3:
                    return True
    return False


if __name__ == '__main__':
    test = [[1, 2, 3, 4, 5], [2, 1, 5, 0, 4, 6], [5, 1, 5, 5, 2, 5, 4]]
    for item in test:
        print('test', item, increasingTriplet(item))
