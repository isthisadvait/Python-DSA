# Author -   Raman Mehta

from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
     def __init__(self) :
        self.head=None
        self.tail=None
        self.count=0


    






     def getSize(self) :
        #Implement the getSize() function
        return self.count



     def isEmpty(self) :
        #Implement the isEmpty() function
        return self.count==0



     def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.count+=1
        temp=Node(data)
        if self.head is None:
            self.head=self.tail=temp
            temp=None
        else:
            self.tail.next=temp
            self.tail=temp
            temp=None
            
            



     def dequeue(self) :
        #Implement the dequeue() function
        ans=-1
        
        if self.head is not None:
            self.count-=1
            ans=self.head.data
            temp=self.head
            self.head=self.head.next
            temp=None
        return ans



     def front(self) :
        #Implement the front() function
        ans=-1
        if self.head is not None:
        
            ans=self.head.data
            
        return ans




#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
