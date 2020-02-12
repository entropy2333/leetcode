class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l + r) // 2
            if (nums[mid] == target):
                return True
            if (nums[mid] == nums[l] == nums[r]):
                l += 1
                r -= 1
            elif (nums[mid] >= nums[l]):
                if (nums[l] <= target < nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if (nums[mid] < target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
        return False

if __name__ == "__main__":    
    target = 6
    nums = [4, 5, 6, 7, 0, 1, 2]
    s = Solution()
    index = s.search(nums, target)
    print(index)