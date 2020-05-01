#code for stack
l=[]
while True:
    n=int(input("Enter 1 to push, 2 to pop , anything else to abort "))
    if n==1:
        l.append(int(input("Enter the element to be pushed ")))
        print("The updated list is ", l)
    elif n==2:
        print(l.pop())
        print("The updated stack is ", l)
    else:
        break