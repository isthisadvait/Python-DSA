
from sys import stdin
import queue

class Stack :

	#Define data members and __init__()
    def __init__(self):
       self.q1 = queue.Queue()
       self.q2 = queue.Queue() 
       self.curr_size = 0






    def getSize(self) :
        return self.curr_size
  



    def isEmpty(self) :
		#Implement the isEmpty() function
        return self.curr_size==0
  

    def push(self, data) :
        self.curr_size += 1
        self.q2.put(data)
        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0]) 
            self.q1.get()
  
        self.q  = self.q1 
        self.q1 = self.q2 
        self.q2 = self.q

    def pop(self) :
        if (self.q1.empty()): 
            return -1
        ans=self.q1.queue[0]
        self.q1.get() 
        self.curr_size -= 1
        return ans


    def top(self) :
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]
  
		




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1
