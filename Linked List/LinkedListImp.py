class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeInput():
    inputList=[int(x) for x in input().split()]
    
    head=None
    tail=None
    
    for data in inputList:
        
        newNode=Node(data)
        
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
    
def printLL(head):
    while head is not None:
        print(head.data,"->",end=' ')
        head=head.next
    print("None")
    return
def length(head) :
    #Your code goes here
    ct=0
    while head is not None:
        ct+=1
        head=head.next
    return ct
def insertAtHeadRec(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    smallhead=insertAtHeadRec(head.next,i-1,data) #induction hypothesis
    head.next=smallhead
    return head
def insertAtI(head,i,data):
    if i<0 and i>length(head):
        return head
    count=0
    prev=None
    cur=head
    while count<1:
        prev=cur
        cur=cur.next
        count=count+1
    newNode=Node(data)
    if prev is not None:
        prev.next=newNode
    else:
        head =newNode
    newNode.next=cur
    return head
def deleteNode(head, pos) :
    # Write your code here.
    if pos<0 or pos>=length(head):
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
        
def lengthRecursive(head):
    # A linked list, find and return the length of input LL recursively.
    # Write your code here

    if head is None:
        return 0
    return 1+lengthRecursive(head.next)
def reverseLinkedListRec(head) :
	#Your code goes here
    if head is None:
        return head
    if head.next is None:
        newNode=head
        return newNode
    newhead=reverseLinkedListRec(head.next)
    head.next.next=head
    head.next=None
    return newhead
def deleteNodeRec(head, pos) :
	#Your code goes here
    if head is None:
        return head
    if pos==0:
        newNode=head.next
        head=None
        return newNode
    small=deleteNodeRec(head.next, pos-1)
    head.next=small
    return head
def midPoint(head) :
    # Write your code here
     if head==None or head.next==None:
            return head
    
     slow=head
     fast=head.next
     while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            
            
            
     return slow

def midPoint(head) :
    # Write your code here
     if head==None or head.next==None:
            return head
    
     slow=head
     fast=head
     while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            
            
            
     return slow
        
def mergeTwoSortedLinkedLists(head1, head2):

    # Write your code here
    returnhead=None
    if head1!=None:
        returnhead=head1
    else:
        returnhead=head2
    if head1==None or head2==None:
        return returnhead
    other =head2
    
    if other.data<returnhead.data:
        returnhead=other
        other=head1
        
    current = returnhead
        
    while current != None and other != None:
        
            if current.next != None and current.next.data < other.data :
                current = current.next
                continue
            else:
                currentNext = current.next
                current.next = other
                current = other
                other = currentNext
            
        
        
    return returnhead

head=takeInput()
printLL(head)
head=insertAtHeadRec(head,2,7)
printLL(head)
