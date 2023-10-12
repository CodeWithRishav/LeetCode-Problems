class Solution:
    def findInMountainArray(self, target: int, nums: 'nums') -> int:
        N = nums.length()
        peek = self.findPeek(target, nums)
        left_index = self.findInAscOrder(target, nums, 0, peek)
        right_index = self.findInDecOrder(target, nums, peek, N - 1)
        if left_index != -1:
            return left_index
        else:
            return right_index

    def findPeek(self, target, nums):
        N = nums.length()
        left, right = 1, N - 2
        while left <= right:
            mid = left + (right - left) // 2
            if nums.get(mid - 1) < nums.get(mid) > nums.get(mid + 1):
                return mid
            elif nums.get(mid - 1) < nums.get(mid) < nums.get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def findInAscOrder(self, target, nums, begin, end):
        left, right = begin, end
        while left <= right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            cur = nums.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def findInDecOrder(self, target, nums, begin, end):
        left, right = begin, end
        while left <= right:
            mid = left + (right - left) // 2
            cur = nums.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1