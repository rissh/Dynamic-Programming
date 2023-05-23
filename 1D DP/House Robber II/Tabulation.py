
def f(arr):
    
    n = len(arr)
    prev = arr[0]
    prev2 = 0
        
    for i in range(1,n):
        pick = arr[i]
        if(i>1):
            pick += prev2
        non_pick = 0 + prev
        curr = max(pick,non_pick)
        prev2 = prev
        prev = curr
            
    return prev

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        arr1 = []
        arr2 = []

        if n == 1:
            return nums[0]

        for i in range(n):
            if i != 0:
                arr1.append(nums[i])
            if i != n - 1:
                arr2.append(nums[i])

        ans1 = f(arr1)
        ans2 = f(arr2)

        return max(ans1, ans2)
