class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        return n == 1

    def isHappy2(self, n):
        happySet = set()
        while n != 1:
            nSum = 0
            while n != 0:
                nSum = nSum + (n % 10) ** 2
                n = n // 10
            if nSum in happySet:
                return bool(0)
            happySet.add(nSum)
            n = nSum
        return bool(1)

if __name__ == '__main__':
    print(Soluiton().isHappy(19))






        """

            Time Complexity = O(k), k is the number of steps to get the happy number
            Space Complexity = O(k)

            Write an algorithm to determine if a number is "happy".
            A happy number is a number defined by the following process: Starting with any positive integer,
            replace the number by the sum of the squares of its digits, and repeat the process until the number
            equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those
            numbers for which this process ends in 1 are happy numbers.

            Example:
            Input:Input: 19
             19 Output:Output: true
             true Explanation:
            Explanati 12 + 92 = 82
            82 + 22 = 68
            62 + 82 = 100
            12 + 02 + 02 = 1
        """
