l=list(map(int, input("Enter the list ").split(" ")))
n=int(input("Enter the element to be searched "))
c=0
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if n== l[mid]:
        c=1
        break
    elif n<l[mid]:
        high=mid-1
    else:
        low=mid+1
if c==1:
    print("Element found")
else:
    print("Element not found")
