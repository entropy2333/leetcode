class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if not d.get(num):
                d[num] = 1
            else:
                d[num] += 1
            if d[num] > n // 2:
                return num

# Boyer-Moore投票算法
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        res=0
        count=0
        for i in range(n):
            if(count==0):
                res=nums[i]
                count=1
            else:
                if(nums[i]==res):
                    count+=1
                else:
                    count-=1
        if(count>0):
            return res