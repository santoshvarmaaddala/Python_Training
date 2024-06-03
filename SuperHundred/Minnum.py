def Min(i,nums):
    if i == len(nums):
        return nums[i-1]
    m = Min(i+1,nums)
    if nums[i-1] < m:
        return nums[i-1]
    return m

print(Min(0,[1,2,0,-1,4,5]))

