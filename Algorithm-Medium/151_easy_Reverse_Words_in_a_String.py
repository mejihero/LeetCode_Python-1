class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        ls = s.split()
        print(ls)

        if ls ==[]: return ""

        ns = ""
        print(len(ls))
        for i in range(0,len(ls)-1):
            ns+=ls[len(ls)-1-i]+" "
        print(ns)
        ns+=ls[0]
        return ns

if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
