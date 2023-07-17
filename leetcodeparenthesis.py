class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        if l < 2 :
            return 0
        ctr = 0
        maxctr = 0
        tracker = -1
        for j in range(1,l):
            #print(index,j)
            print(j)
            if s[j] == ')':
                print('inside')
                #check previous entry
                tracker = j-1 if tracker < 0 else tracker
                if s[tracker] == '(':
                    print('inside (')
                    ctr = ctr + 2
                    tracker = tracker - 1 if tracker > 0 else -1
                    maxctr = ctr if ctr > maxctr else maxctr
                else:
                    tracker = tracker + 1
                    maxctr = ctr if ctr > maxctr else maxctr
                    ctr = 0
                    
            
         
        print(maxctr)
        return maxctr
        

if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses("(((()()())))")