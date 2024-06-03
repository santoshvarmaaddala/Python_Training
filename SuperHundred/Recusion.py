def Printn(i,n):
    print(i)
    if i >= n:
        return
    Printn(i+1,n)


Printn(3,9)  