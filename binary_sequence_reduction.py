t = int(input())
while(t!=0):
    m=int(input())
    s=input()
    a = []
    for i in range(len(s)):
        a.append(s[i])
    c=0
    while(True):
        c=c+1
        x=a[0]
        a.pop(0)
        n=len(a)
        j=0
        while(True):
            if j>=n:
                break
            if x=='0':
                if a[j] == '1':
                    a.pop(j)
                    x='1'
                else:
                    j=j+1
            elif x=='1':
                if a[j] == '0':
                    a.pop(j)
                    x='0'
                else:
                    j=j+1
            n=len(a)
        if a == []:
            break
    print(c)
    t=t-1
