#linear searching through an integer list 'l'
l=list(map(int, input("Enter the list ").split(" ")))
n=int(input("Enter the element to be searched "))
c=0
for i in l:
    if i==n:
        c=1
        break
if c==1:
    print("Element found")
else:
    print("Element not in the list")