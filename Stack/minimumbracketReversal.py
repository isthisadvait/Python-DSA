                     #Author -Raman Mehta
from sys import stdin

def countBracketReversals(inputString) :
    # Your code goes here
    st=[]
    ans=0
    for char in inputString:
        if char=='{':
            st.append(char)
        else:
            if len(st)!=0:
                st.pop()
            else:
                st.append('{')
                ans+=1
                
    if len(st)%2==0:
        return ans+len(st)//2
    else:
        return -1

      
      #main
print(countBracketReversals(stdin.readline().strip()))
