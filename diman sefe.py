k=1
j=1
while j<5:
    a=1
    while a<5-j:
        print("",end="")
        a=a+1
    n=1
    while n<=k:
        print("",end="*")
        n=n+1
    k=k+2
    print()
    j=j+1
k=9
j=1
while j<=5:
    a=1
    while a<=j-5:
        print("",end="") 
        a=a+1
    n=1
    while n<=k:
        print("",end="*")
        n=n+1
    k=k-2
    print()
    j=j+1
print(j)