class SlidingWindow:
    def find_length(nums, k):
        left = 0
        curr = 0
        ans = 0

        for right in range(0, len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            
            ans = max(ans, right-left+1)
        return ans

nums = [3,1,2,7,4,2,1,1,5]
print(SlidingWindow.find_length(nums, 8))