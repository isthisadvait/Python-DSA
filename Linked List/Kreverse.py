#Author - Raman Mehta
#Reverse LL in groups of K
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def kReverse(head, k) :
	#Your code goes here
    if head is None or k==1 or k==0:
        return head
    current = head
    next = None
    prev = None
    count = 0
 

    while current != None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count+=1
    
 

    if next != None:
        head.next = kReverse(next, k)
 
    
    return prev



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
