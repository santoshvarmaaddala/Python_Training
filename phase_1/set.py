"""
# union

a = {1,2,3}
b = {1,4,5}
c = a.union(b)
print(c)
print(a|b,a,b)
print(a.update(b),a,b)
"""
"""
# intersection
a = {1,2,3}
b = {1,4,5}
c = a.intersection(b)
print(c)
print(a&b,a,b)
print(a.intersection_update(b),a,b)
"""
"""
#difference
a = {1,2,3}
b = {1,4,5}
c = a.difference(b)
print(c)
print(a-b,a,b)
print(a.difference_update(b),a,b)
"""

#symmetric diiference
a = {1,2,3}
b = {1,4,5}
c = a.symmetric_difference(b)
print(c)
print(a^b,a,b)
print(a.symmetric_difference_update(b),a,b)
