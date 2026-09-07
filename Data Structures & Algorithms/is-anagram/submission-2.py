class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=[]
        t_list=[]
        for i in range(len(s)):
            s_list.append(s[i])
        for j in range(len(t)):
            t_list.append(t[j])

        s_list.sort()
        t_list.sort()
        if s_list==t_list:
            return True
        else:
            return False
