class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            #print(mid)
            if mid > num / mid:
                right = mid - 1
            elif mid == num/mid:
                return True
            else:
                left = mid + 1
        return left == num // left and num % left == 0

if __name__ == '__main__':
    print(Solution().isPerfectSquare(4))






    """
        Time Complexity = O(log(n))
        Space Complexity = O(1)

        Given a positive integer num, write a function which returns True if num is a perfect square else False.
        Note: Do not use any built-in library function such as sqrt.

        Example:
        Input: 14
        Output: false
    """
