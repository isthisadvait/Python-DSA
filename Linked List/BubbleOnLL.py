#Author Raman Mehta
#bubble Sort On LL
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def bubbleSort(head) :
	#Your code goes here
    swap = 0
    if head != None:
         while(1):
           swap = 0
           tmp = head
           while(tmp.next != None):
                if tmp.data > tmp.next.data:
                        # swap them
                        swap += 1
                        p = tmp.data
                        tmp.data = tmp.next.data
                        tmp.next.data = p
                        tmp = tmp.next
                else:
                        tmp = tmp.next

           if swap == 0:
                    break
           else:
                    continue


         return head
    else:
            return head




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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
