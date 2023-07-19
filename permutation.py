class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        a=len(nums)
        for i in range(a):
            ans.append(nums[nums[i]])
        return ans
