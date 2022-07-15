#！ -*- coding: utf-8 -*-

class Solution:
    def permute(self, nums):
        result = []

        def back(new_nums):
            if len(new_nums) == len(nums):
                result.append(new_nums.copy())
                return
            for num in nums:
                if num in new_nums:
                    continue
                new_nums.append(num)
                back(new_nums)
                new_nums.pop(-1)
        back([])
        return result