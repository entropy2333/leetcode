# 60ms
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s == '':
#             return 0
#         max_len = 0
#         tmp_list = []
#         for ch in s:
#             # print(tmp_list, max_len)
#             if tmp_list == []:
#                 tmp_list.append(ch)
#                 max_len = 1
#                 continue
#             if ch in tmp_list:
#                 max_len = max(max_len, len(tmp_list))
#                 tmp_list = tmp_list[tmp_list.index(ch)+1:]
#                 tmp_list.append(ch)
#             else:
#                 tmp_list.append(ch)
#                 max_len = max(max_len, len(tmp_list))

#         return max_len

# l = ['abcabcbb']
# for s in l:
#     print(Solution().lengthOfLongestSubstring(s))

# 用字典的方法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: # 字符串为空
            return 0
        if len(s)==1:
            return 1
        max_len = 0
        start = 0
        hash_map = {} # hash_map也即字典
        for i,e in enumerate(s):
            # 如果e在字典中，start记录重复元素的后一位索引
            if e in hash_map and start <= hash_map[e]:
                start = hash_map[e]+1
            else:
                max_len = max(max_len,i-start+1)
            hash_map[e] = i
        return max_len
