class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        minimum=1000000
        subSum=0
        while right<len(nums):
            subSum += nums[right]
            while subSum>=target:
                minimum=min(minimum,right-left+1)
                subSum -= nums[left]
                left+=1
            right+=1
        return 0 if minimum ==1000000 else minimum
