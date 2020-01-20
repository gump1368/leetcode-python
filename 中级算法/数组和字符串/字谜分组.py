"""
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def count_char(s):
            count = {}
            for char in s:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 0
            return count

        strs = [(s, count_char(s)) for s in strs]

        strs_dict = {}
        for s in strs:
            l = len(s[0])
            if l in strs_dict.keys():
                strs_dict[l].append(s)
            else:
                strs_dict[l] = [s]

        res = []
        for values in strs_dict.values():
            i = 0
            while i < len(values):
                count_str = values[i]
                cache = [count_str[0]]
                start = i+1
                for j in range(start, len(values)):
                    next_str = values[j]
                    if count_str[1] == next_str[1]:
                        cache.append(next_str[0])
                        values[i+1], values[j] = values[j], values[i+1]
                        i += 1
                res.append(cache)
                i += 1

        return res


if __name__ == '__main__':
    solution = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))
