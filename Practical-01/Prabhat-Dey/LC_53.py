class Solution(object):
    def maxSubArray(self, nums):
        a=nums[0]
        sum=0
        for i in nums:
            sum+=i
            if sum>a:
                a=sum
            if sum<0:
                sum=0
        return a