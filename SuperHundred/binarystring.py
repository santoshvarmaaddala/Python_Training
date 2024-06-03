def PrintBinaryStr(index,s,n):
    if index == n:
        print(s)
        return 
    PrintBinaryStr(index+1,s+"1",n)
    PrintBinaryStr(index+1,s+"0",n)
    
PrintBinaryStr(0,"",4)