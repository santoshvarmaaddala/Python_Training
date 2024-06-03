def maX(i,nums):
    if i == len(nums):
        return nums[i-1]
    s = maX(i+1,nums)
    if s > nums[i]:
        return s
    else:
        return nums[i]
    
print(maX(0,[1,2,5]))
    

    
