class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[:1:-1]
        return int(b + '0'*(32-len(b)), 2)

    def reverseBits1(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

    def reverseBits2(self, n):
        string = bin(n)
        if '-' in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)

if __name__ == '__main__':
  print(Solution().reverseBits(1))






        """

            Time Complexity = O(log(n))
            Space Complexity = O(1)

            Reverse bits of a given 32 bits unsigned integer.

            Example:
            Input: [1,2,3,4,5,6,7] and k = 3
            Output: [5,6,7,1,2,3,4]
            Explanation:
            Input: 43261596
            Output: 964176192
            Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
                         return 964176192 represented in binary as 00111001011110000010100101000000.

            Not only fully understand with the result.

        """
