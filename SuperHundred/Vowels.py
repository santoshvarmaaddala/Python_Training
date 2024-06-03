def Vowels(s,index):
    if index == len(s):
        return 0
    count = Vowels(s,index+1)
    if s[index] in "aAeEIiOoUu":
        return count+1
    return count

print(Vowels("HelloWorld",0))