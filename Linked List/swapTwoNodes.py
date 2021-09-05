#Author-> Raman Mehta
#Swap two Nodes without swapping data. You are given two position.
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
	#Your code goes here
        if i== j:
            return head

        curr_i = head
        curr_j = head
        prev_i = None
        prev_j = None

        # find node with pos i
        l=0
        while l!=i:
            prev_i = curr_i
            curr_i = curr_i.next
            l+=1

        # find node with pos j
        k=0
        while k!=j:
            prev_j = curr_j
            curr_j = curr_j.next
            k+=1

        # pos i or j is not there
        if curr_i is None or curr_j is None:
            return head

        # if i is not head of the linked list.
        if prev_i is not None:
            prev_i.next = curr_j
        else: # if i was head, make j the head of the linked list.
            head = curr_j

        # if j is not head of the linked list
        if prev_j is not None:
            prev_j.next = curr_i
        else: # if j was head, make i the head of the linked list.
            head = curr_i

        # now swap the next pointers.
        temp = curr_i.next
        curr_i.next = curr_j.next
        curr_j.next = temp
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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
