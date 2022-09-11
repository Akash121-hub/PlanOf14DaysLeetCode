nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
MAxsub = nums[0]
CurSum = 0

for i in nums:
    if CurSum < 0:
        CurSum = 0
    CurSum += i 
    MAxsub = max(MAxsub,CurSum)
print(MAxsub)
        
