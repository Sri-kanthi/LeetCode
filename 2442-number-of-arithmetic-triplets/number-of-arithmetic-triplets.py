class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0
        for num in nums:
            if num + diff in nums and num + diff*2 in nums:
                count += 1
        return count