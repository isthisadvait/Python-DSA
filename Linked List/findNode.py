# Author Raman Mehta
#Find a node ,return it's position(0 based) if not found return -1
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    i=0
    ans=-1
    while head!=None:
        if head.data == n:
            ans=i
            break
        else:
            head=head.next
            i+=1
    return ans
