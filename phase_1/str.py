s = "hgf hGf abdh"
for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

print(s[1:6:3],s[::],s[::-1])

# str functions

x = s.capitalize()
print(x)
print(x.isalpha())

print(x.isalnum())
print(s.split())
print(s.split("h",maxsplit=1))
print(s.partition("h"))
print(s.encode())

#str formatting
a = 4
b = 5
print(f"addition of {a} and {b} is {a+b}")
print("addition of {0} and {1} is {2}".format(a,b,a+b))