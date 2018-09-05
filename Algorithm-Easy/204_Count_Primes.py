class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        num = n/2
        for i in range(3, n, 2):
            if i * i >= n:
                break
            if not is_prime[i]:
                continue

            for j in range(i*i, n, 2*i):
                if not is_prime[j]:
                    continue

                num -= 1
                is_prime[j] = False

        return int(num)

if __name__ == '__main__':
    print(Solution().countPrimes(10))






        """

            Time Complexity = O(n)
            Space Complexity = O(n)

            Count the number of prime numbers less than a non-negative number, n.

            Example:
            Input: 10
            Output: 4
            Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
        """
