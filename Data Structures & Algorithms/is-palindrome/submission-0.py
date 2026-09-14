class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_string = "".join(filter(str.isalnum,s))
        cleaned_string = cleaned_string.lower()
        s=cleaned_string
        l,r=0,len(s)-1
        while l<r:
             
            if s[l]!=s[r]:
                return False
            
            l+=1
            r-=1
        return True