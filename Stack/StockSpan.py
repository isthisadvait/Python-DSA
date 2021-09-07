from sys import stdin

def stockSpan(price, n) :
	#Your code goes here
    stockspan = []
    stack = [] # Creating an empty stack

    # Base case
    stockspan.append(1)
    stack.append(0)
    for i in range(1, n):

      # Pop elements out of stack until either: 1) The stack gets empty
      #or 2) the rate at stack top turns out to be larger than the rate
      #at the current element
      while price[i] > price[stack[-1]]:
        stack.pop()

        if len(stack) is 0:
          break
      
      # Set the stockspan values.
      if len(stack) > 0:
          stockspan.append(i - stack[-1])
      else:
          stockspan.append(i + 1) 

      stack.append(i)
    
    return stockspan






'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
