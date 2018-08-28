class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

if __name__ == "__main__":
    print(Solution().plusOne([6, 9, 9, 9]))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each
        element in the array contain a single digit.
        You may assume the integer does not contain any leading zero, except the number 0 itself.

        Example:
        Input: [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
    """
