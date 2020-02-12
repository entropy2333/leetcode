def binary_search(nums, target, flag=True):
    low = 0
    high = len(nums)

    while low < high:
        mid = (low + high) // 2
        if target < nums[mid] or (flag and target == nums[mid]):
            high = mid
        else:
            low = mid+1
    return low if flag else low - 1

if __name__ == "__main__":    
    target = 8
    nums = [1, 4, 5, 8, 8, 8, 9]
    left = search(nums, target, flag=True)
    right = search(nums, target, flag=False)
    print(left, right)