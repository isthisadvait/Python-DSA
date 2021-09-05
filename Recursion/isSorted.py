#DSA with Python By Raman Mehta
#Given a List check if it is sorted
def isSorted(arr,si):
    n=len(arr)
    if si==n-1 or si==n:
        return True
    if arr[si]>arr[si+1]:
        return False
    return isSorted(arr,si+1)
arr=[1,12,4,5,7]
print(isSorted(arr,0))
