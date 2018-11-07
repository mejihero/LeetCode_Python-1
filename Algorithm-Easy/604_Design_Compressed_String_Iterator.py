class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.curr_char = ""
        self.curr_count = 0
        self.index = 0
        self.string = compressedString


    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.curr_count -= 1
            return self.curr_char
        return " "


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr_count:
            return True
        else:
            if self.index+1 < len(self.string):
                self.curr_char = self.string[self.index]
                curr = ""
                for index, char in enumerate(self.string[self.index+1:]):
                    curr += char
                    if self.RepresentsInt(curr):
                        self.curr_count = int(curr)
                    else:
                        break
                self.index += index + 1
                return True
            else:
                return False

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()






  """
        Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

        The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

        next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
        hasNext() - Judge whether there is any letter needs to be uncompressed.

        Note:
        Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

        Example:

        StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

        iterator.next(); // return 'L'
        iterator.next(); // return 'e'
        iterator.next(); // return 'e'
        iterator.next(); // return 't'
        iterator.next(); // return 'C'
        iterator.next(); // return 'o'
        iterator.next(); // return 'd'
        iterator.hasNext(); // return true
        iterator.next(); // return 'e'
        iterator.hasNext(); // return false
        iterator.next(); // return ' '

  """
