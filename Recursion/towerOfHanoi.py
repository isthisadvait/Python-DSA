#Tower Of Hanoi by Raman Mehta
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n==1:
        print(source,dest,end=" ")
        print()
        return
    if n==0:
        return
    towerofhanoi(n-1,source,dest,aux)
    print(source,dest,end=" ")
    print()
    towerofhanoi(n-1,aux,source,dest)
    
    

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')
