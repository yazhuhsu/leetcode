class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        if s[len(s)-1] == '(' or s[len(s)-1] == '[' or s[len(s)-1] == '{':
            return False
        
        ss = []
        ss_len = 0
        for i in range(0, len(s)):
            if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
                ss.append(s[i])
                ss_len+=1
            elif(s[i] == ')'):
                if(ss[ss_len-1] != '('):
                    return False
                elif(ss[ss_len-1] == '('):
                    ss.pop()
                    ss_len-=1
            elif(s[i] == ']'):
                if(ss[ss_len-1] != '['):
                    return False
                elif(ss[ss_len-1] == '['):
                    ss.pop()
                    ss_len-=1
            elif(s[i] == '}'):
                if(ss[ss_len-1] != '{'):
                    return False
                elif(ss[ss_len-1] == '{'):
                    ss.pop()
                    ss_len-=1
                    
        return True
            
        