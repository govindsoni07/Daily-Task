nums=[1,0,1,2,0,3,0,10]
i=0
for j in range(len(nums)):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
print(nums)