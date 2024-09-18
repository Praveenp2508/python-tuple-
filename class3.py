#tuple

eg=(2,'hi','okey','false',5,5,5,5)

print(eg[2:5])
print(eg[4])

#count

print(eg.count(5))

#changing tuple to list

r=list(eg)
print(type(r))

r.insert(3,'you')
print(r)

#nestedtuple

nest=[500,(8,8,'hat','jam'),(2,'hi','okey','false',5,5,5,5)]

print(nest[1][3])

#set---------- {} / set()

set={2,3,6,5,4,7,2,7,5,5,1}
print(set)

thisset={'apple','banana','cherry'}
thisset.discard(5)
print(thisset)

a,b= {2,45,7,9,23},{43,6,7,9,2}
print(a.difference(b))
print(a)
b.difference_update(a)
print(b)

