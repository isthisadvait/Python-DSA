
from sys import stdin
import queue

def reverseKElements(q, k) :
    #Your code goes here
    n = q.qsize()

    a = []

    # Insert elements present in the queue into the array
    for i in range(n):
        a.append(q.get())

    # Reverse the first K element of the array
    a = list(reversed(a[0:k])) + a[k:]

    for i in range(n):
        q.put(a[i])

    # Return the queue
    return q







'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
