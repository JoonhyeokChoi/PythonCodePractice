class TwoPointers:
    def checkIfPalindrome(s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    
    def checkForTarget(nums, target):
        left = 0
        right = len(nums) -1

        while left < right:
            current = nums[left] + nums[right]

            if current == target:
                return True
            
            if current > target:
                right-=1
            else:
                left+=1
        return False
    
    def combine(arr1, arr2):
        i = 0
        j = 0
        ans = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i+=1
            else:
                ans.append(arr2[j])
                j+=1
        
        while i < len(arr1):
            ans.append(arr1[i])
            i+=1

        while j < len(arr2):
            ans.append(arr2[j])
            j+=1

        return ans
    
    def isSequence(s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1

        return i == len(s)

    
print(TwoPointers.isSequence("ace", "abcde"))