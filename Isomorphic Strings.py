class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        checked = [0] * len(s)
        for i in range(len(s)):
            if checked[i] == 0:
                checked[i] = 1
                for j in range(i + 1, len(s)):
                    if s[j] == s[i]:
                        if t[j] == t[i]:
                            checked[j] = 1
                        else:
                            return False
                    elif t[j] == t[i]:
                        return False

        for c in checked:
            if c == 0:
                return False

        return True