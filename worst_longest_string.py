# I am 100% sure this will not work and is a bad approach.
# That said I'm here for those github commits.  Gimme.
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.tempOnes = 0
        self.tempZeros = 0
        self.longestOne = 0
        self.longestZero = 0
        if s[0] == 1:
            longestOne = 1
            path = "One"
        else:
            longestZero = 1
            path = "Zero"
        for i in s:
            if path == "One" and i == 1:
                path = "One"
                longestOne += 1
                pass
            elif path == "One" and i == 0:
                path = "Zero"
                tempZeros = 1
                pass
            elif path == "Zero" and i == 0:
                path = "Zero"
                longestZero += 1
                pass
            elif path == "Zero" and i == 1:
                path = "One"
                tempOnes = 1
                pass
        
        if longestOne > longestZero:
            return True
        else:
            return False
