# Parent to Child
def PToCSumOfList(i,n,nums,Sum):
    if i == n:
        print(Sum)
        return Sum
    Sum += nums[i]
    PToCSumOfList(i+1,n,nums,Sum)
    
#PToCSumOfList(0,3,[1,3,4],0)

# Child to Parent
def  CToPSumOfList(i,n,nums):
    if i == n:
        return 0
    total = CToPSumOfList(i+1,n,nums)
    return total + nums[i]
print(CToPSumOfList(0,3,[1,2,3]))
