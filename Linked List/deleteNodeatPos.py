#Author Raman Mehta
#delete Node From Singly Linked List at gven Position
from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def Length(head) :
    #Your code goes here
    ct=0
    while head is not None:
        ct+=1
        head=head.next
    return ct
def deleteNode(head, pos) :
    # Write your code here.
    if pos<0 or pos>=Length(head):
        return head
    prev=None
    cur=head
    while pos!=0 and cur is not None:
            prev=cur
            cur=cur.next
            pos-=1

    if cur!=None and prev!=None:
        prev.next=cur.next
        cur=None
    elif cur==None:
        prev.next=None

    elif prev==None:
        prev=cur.next
        head=prev
        cur=None
    return head


















# Taking Input Using Fast I/O.
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



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
