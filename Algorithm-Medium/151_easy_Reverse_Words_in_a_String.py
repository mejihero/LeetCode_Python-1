class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        ls = s.split()
        if ls ==[]: return ""
        ns = ""
        for i in range(0,len(ls)-1):
            ns+=ls[len(ls)-1-i]+" "
        ns+=ls[0]
        return ns
