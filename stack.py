m=[]
while True:
    n=int(input("Enter 1 to push, 2 to pop , anything else to abort "))
    if n==1:
        m.append(int(input("Enter the element to be pushed ")))
        print("The updated list is ", m)
    elif n==2:
        print(m.pop())
        print("The updated stack is ", m)
    else:
        break
