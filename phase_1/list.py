# taking list from input
"""
l = input().split()
print(l,type(l))

# converting list into list(int)

for i in range(len(l)):
    l[i] =int(l[i])
print(l,type(l))

# list comprehension
l = [int(i) for i in input().split()]
print(l,type(l))
"""
'''
# map class
l = list(map(int,input().split()))
print(l)
'''
"""
#adding elements i list

l = [3, 6, 9]
l = list(map(lambda x: x*x,l))
print(l)
# filter class
p = list(filter(lambda y: y%2==1,l))
print(p)

j = [i*i for i in l if i%2==0]
j.append(10)
j.extend([8,0,0])
j.insert(3,90)
print(j)


# deleting elements in list
q = [0,3,"34"]
print(q.pop(2))
print(q)
q.remove(0)
print(q)
q.clear()
print(q)
"""

#sort func

a = [3,2,7,4,9]
a.sort(reverse=True)
print(a)
b = sorted(a)
c = [[22,3],[43,54],[0,0],[0,1],[6,56]]
print(sorted(c,key = sum))
print(sorted(c,key = lambda x : x[1]))

d = [0,9,8]
l = [0] * 5
print(a+[0],a*2,l)
l[1] = 2
print(l)
p = [i+2 for i in l if i == 0]
print(p)
 