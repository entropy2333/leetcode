# 32ms
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         return os.path.commonprefix(strs)

# 20ms
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        # zip(*strs)返回一个由元组组成的list
        for item in zip(*strs):
            # 对于每一项使其集合化，若只有一个元素则为公有字符
            tmp_set = set(item)
            if len(tmp_set) == 1:
                res += item[0]
            else:
                break
        return res