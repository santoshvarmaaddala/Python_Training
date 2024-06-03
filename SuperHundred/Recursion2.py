def Recursion(i,n):
    if i >= n:
        print("Base condition got hit")
        return 
    print("Ending line", i)
    for j in range(1,i):
        print(j,end =" ")
    print()
    Recursion(i+1,n)
    print("Starting line",i)

Recursion(1,4)