class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 0:
            result += n // 5
            n = n // 5
        return result

if __name__ == "__main__":
    print(Solution().trailingZeroes(11))






    """
            Time Complexity = O(log(n))
            Space Complexity = O(1)

            Given an integer n, return the number of trailing zeroes in n!.

            Example:
            Input: 3
            Output: 0
            Explanation: 3! = 6, no trailing zero.

            思路：
            当出现0，也就是10的N次方，可以推论一定要出现组合2 & 5
            数字2在很多数字中都以提取出来，所以决定有多少个0的是基于所包含的数字5的个数
            比如当n = 5， 5*4*3*2*1 = 120，这边就只有一个0
    """
