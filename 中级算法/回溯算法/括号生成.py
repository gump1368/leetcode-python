#！ -*-coding: utf-8 -*-


class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []

        def is_valid(s):
            bal = 0
            for i in s:
                if i == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        results = []

        def back_up(res, l, r):
            temp_l = ['(', ')']
            for s in temp_l:
                if l > n or r > n:
                    break
                res += s
                if len(res) == 2 * n:
                    if is_valid(res):
                        results.append(res)
                    res = res[:-1]
                elif s == '(':
                    res = back_up(res, l + 1, r)
                else:
                    res = back_up(res, l, r + 1)
            return res[:-1]

        back_up('(', 0, 0)
        return results