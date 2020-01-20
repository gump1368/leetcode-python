"""
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        palindrome_dict = {}
        char_dict = {}
        max_palindrome = s[0]
        for i, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = [i]
            else:
                for j in char_dict[char]:
                    sub_s = s[j:i+1]
                    key = len(sub_s)-2
                    if (key in palindrome_dict and sub_s[1:-1] in palindrome_dict[key]) or len(sub_s[1:-1]) <= 1:
                        max_palindrome = sub_s if len(sub_s) > len(max_palindrome) else max_palindrome
                        key_new = len(sub_s)
                        if key_new in palindrome_dict:
                            palindrome_dict[key_new].append(sub_s)
                        else:
                            palindrome_dict[key_new] = [sub_s]
                        break

                char_dict[char].append(i)
        return max_palindrome


if __name__ == '__main__':
    test_s = ['babad', 'ac', 'babadada', 'a', '', 'abacab', 'aaaa', 'aaabaaaa', 'ababababababa']
    solution = Solution()
    for s in test_s:
        print('longest palindrome of {} is {}'.format(s, solution.longestPalindrome(s)))

