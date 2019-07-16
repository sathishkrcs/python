# Core Data Types
#They are defined as int, float and complex class in Python.

a = 10;
print(a, 'type of', type(a)); #int type

a = 10.23;
print(a, 'type of', type(a)); #float type

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

b = 'Sathish';
print(b, 'type of', type(b)); #str type

#List
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("a[2] = ", a[2])
print("a[0:3] = ", a[0:3])
print("a[5:] = ", a[5:])

#Tuples(Im-mutable)

t = (1,2,3, 'Kriya', 5+2j)
print(t)

#String
s = 'United States of America'
print(s[0:6])
print(s[6:])
print(s[-6:])
print(type(s[:7]))

#Set
a = {1,2,3,3,4,6,5,2,5,3,8,55,98,67,44,66,66}
b = {2,3,5,2345}
print(a)
print(a.union(b))

#Dictionay
d = [{"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}]

print(d[0]['firstName'])



