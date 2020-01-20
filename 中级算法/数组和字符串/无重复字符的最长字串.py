"""
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans

        # max_interval = 0
        # for i in range(len(s)):
        #     j = i+1
        #     offset = 1
        #     while j < len(s):
        #         char2 = s[j]
        #         if char2 in s[i:j]:
        #             break
        #         else:
        #             offset += 1
        #         j += 1
        #     max_interval = max(offset, max_interval)
        #
        # return max_interval





if __name__ == '__main__':
    test = ['pwwkew', 'abcabcbb', 'pwwkew', 'cdd', 'abba', '']
    solution = Solution()
    for t in test:
        res = solution.lengthOfLongestSubstring(t)
        print('max length of {} is {}'.format(t, str(res)))

