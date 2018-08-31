class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            print('n',n)
            n &= n - 1
            print(n)
            result += 1
        return result

if __name__ == '__main__':
  print(Solution().hammingWeight(3))






        """

            Time Complexity = O(1)
            Space Complexity = O(1)

            The run time depends on the number of 11-bits in nn. In the worst case, all bits in nn are 11-bits.
            In case of a 32-bit integer, the run time is O(1)O(1).
            The space complexity is O(1)O(1), since no additional space is allocated.

            Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known
            as the Hamming weight).

            Example:
            Input: 11
            Output: 3
            Explanation: Integer 11 has binary representation 00000000000000000000000000001011

            References: https://leetcode.com/problems/number-of-1-bits/solution/

        """
