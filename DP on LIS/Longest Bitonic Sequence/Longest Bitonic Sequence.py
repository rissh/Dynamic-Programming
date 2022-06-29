
def longestBitonicSequence(arr, n):
    # Write your code here.
    N = len(arr)
    
    dp1 = [1]*N    
    for i in range(1, N):
        for j in range(i-1, -1, -1):
            if (1 + dp1[j] > dp1[i]) and arr[j] < arr[i]:
                dp1[i] = 1 + dp1[j]
                
    dp2 = [1]*N    
    for i in range(N-1,-1,-1):
        for j in range(N-1, i-1, -1):
            if (1 + dp2[j] > dp2[i]) and arr[j] < arr[i]:
                dp2[i] = 1 + dp2[j]            
    
    res = 0
    for i in range(N):
        res = max(res,dp1[i]+dp2[i]-1)
    return res
  
