class Solution:
    def isPalindrome(self, s: str) -> bool:
        seen=[]
        for i in range(len(s)):
            if s[i].isalnum():
                seen.append(s[i].lower())

        seen_reverse=seen[::-1]

        if seen == seen_reverse:
            return True
        else:
            return False


        
        