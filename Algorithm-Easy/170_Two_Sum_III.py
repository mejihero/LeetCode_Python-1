from collections import defaultdict
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.lookup[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (num != key or self.lookup[key] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

if __name__ == "__main__":
    Sol = TwoSum()

    for i in (1, 3, 5):
        Sol.add(i)

    for i in (4, 7):
        print(Sol.find(i))






    """
            Time Complexity = O(n)
            Space Complexity = O(n)

            Design and implement a TwoSum class. It should support the following operations: add and find.
            add - Add the number to an internal data structure.
            find - Find if there exists any pair of numbers which sum is equal to the value.

            Example:
            add(1); add(3); add(5);
            find(4) -> true
            find(7) -> false
    """
