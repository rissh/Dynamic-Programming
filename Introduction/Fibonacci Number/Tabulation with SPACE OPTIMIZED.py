
class Solution:
    def fib(self, n: int) -> int:

        if n==0:
            return 0

        prev = 1
        prev2 = 0

        i = 2
        while(i <= n):
            curr = prev + prev2
            prev2 = prev
            prev = curr
            i += 1

        return prev
