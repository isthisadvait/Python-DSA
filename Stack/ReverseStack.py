#Reverse Stack Using One Extra Stack                           Author -Raman Mehta
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def transfer(s1, s2, n):
     
    for i in range(n):
 
        # Store the top element
        # in a temporary variable
        temp = s1[-1]
 
        # Pop out of the stack
        s1.pop()
 
        # Push it into s2
        s2.append(temp)
def reverseStack(inputStack, extraStack) :
	#Your code goes here
    n=len(inputStack)
    for i in range(n):
 
        # Store the top element
        # of the given stack
        x = inputStack[-1]
 
        # Pop that element
        # out of the stack
        inputStack.pop()
 
        transfer(inputStack, extraStack, n - i - 1)
        inputStack.append(x)
        transfer(extraStack, inputStack, n - i - 1)


'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
