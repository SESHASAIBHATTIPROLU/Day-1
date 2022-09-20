class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        try:
            s = float(s)
            return True
        except:
            return False
ob = Solution()
print(ob.isNumber("0.2"))
print(ob.isNumber("abc"))
print(ob.isNumber("Hello"))
print(ob.isNumber("-2.5"))
print(ob.isNumber("10"))
