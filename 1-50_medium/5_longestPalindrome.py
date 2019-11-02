# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if not s:
#             return s
#         if len(s) == 1:
#             return s
#         tmp_str = ''
#         tmp_list = []
#         for ch in s:
#             print(tmp_str, tmp_list)
#             if tmp_str == '':
#                 tmp_str += ch
#                 continue
#             # 如果有相同字符，则有回文的可能
#             if ch in tmp_str:
#                 # tmp为可能回文的字符串
#                 tmp = tmp_str[tmp_str.index(ch):]
#                 tmp += ch
#                 print('tmp:%s'tmp)
#                 # tmp为回文字符串，则tmp_str也可能回文 此时tmp_str = %s + tmp
#                 if tmp == tmp[::-1]:
#                     tmp_str += ch
#                     if not tmp_list:
#                         tmp_list.append(tmp)
#                     elif len(tmp) > len(tmp_list[0]):
#                         tmp_list.pop()
#                         tmp_list.append(tmp)
#                 else:
#                 # tmp不是回文字符串
#                     tmp_str = tmp_str[tmp_str.index(ch)+1:]
#                     tmp_str += ch
#             else:
#                 tmp_str += ch
#         if not tmp_list:
#             return s[-1]
#         return tmp_list[0]

# # 因为不管多复杂的字符串都可能是回文的，只要另一半对称就行，所以必须得继续遍历且保留之前的字符串，那么我的朴素想法就做不出来了
# s = 'aaabaaaa'

# # print(s.index('a'),s.index('b'))
# print(Solution().longestPalindrome(s))

# 动态规划，选择copy别人代码
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用（防止下标越界）
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res

# 中心扩散
class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size == 0:
            return ''

        # 至少是 1
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub

        return longest_palindrome_str

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        l = left
        r = right

        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1
