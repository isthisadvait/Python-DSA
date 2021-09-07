#Author-Raman Mehta
from sys import stdin


def isBalanced(expression) :
	#Your code goes here
    s=[]
    for char in expression:
        if char=='(':
            s.append(char)
        else:
            if len(s)==0:
                return False
            else:
              s.pop()
    if len(s)==0:
        return True
    else :
        return False







#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
