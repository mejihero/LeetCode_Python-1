class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        return sum(self.getFactors(num)) == num


    def getFactors(self, num):
        sqrt_num = int(math.sqrt(num))

        # 1 is always a factor
        factors = set([1])

        # Start from 2
        for i in range(2, sqrt_num+1):
            print(i)
            if num % i == 0:
                factors.add(i)
                print('1',factors)
                factors.add(num//i)
                print('2',factors)

        return factors






        """
        We define the Perfect Number is a positive integer that is equal to the sum of all
        its positive divisors except itself.

        Now, given an integer n, write a function that returns true when it is a perfect
        number and false when it is not.

        Example:
        Input: 28
        Output: True
        Explanation: 28 = 1 + 2 + 4 + 7 + 14
        Note: The input number n will not exceed 100,000,000. (1e8)
        """
