#Author Raman Mehta
#Problem -Arrange even numbers after all odd numbers in a SLL
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    if head is None or head.next is None:
        return head
    
    
    prev=None
    cur=head
    temp1=None
    temp2=None

    
    while cur is not None:
        if cur.data%2 != 0:
            if prev is None:
                prev=cur
                head=prev
                cur=cur.next
            else:
                prev.next=cur
                cur=cur.next
                prev=prev.next
                
        else:
            if temp2 is None:
                temp2=cur
                temp1=temp2
                cur=cur.next
                temp2.next=None
            else:
                temp2.next=cur
                cur=cur.next
                temp2=temp2.next
                temp2.next=None
      
    if prev is not None:
     prev.next=temp1
    else :
        head=temp1
    return head
            
            



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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
