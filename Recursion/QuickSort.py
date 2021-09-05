#QuickSort In Python By -Raman Mehta
def partition(arr,start,end):
    x=arr[end];
    i=start-1;
    for j in range(start,end):
      if arr[j]<=x:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
                     
            
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1

def quickSort(arr, start, end):
    # Please add your code here
    if start<end:
        q=partition(arr,start,end)
        quickSort(arr,start,q-1)
        quickSort(arr,q+1,end)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
