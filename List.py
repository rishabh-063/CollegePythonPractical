
l =[]

list1 = [1,2,"abc",3,[4,5]]

list2 = []

list3 = list((1,2,3))



# append

list1.append(6)

# insert 

list1.insert(1,'a')

# pop

list1.pop()

list1.pop(1)  # with index

# sorting

list4 = [100,5,2,6,1]
list4.sort()
list4.sort(reverse=True)

newlist = sorted(list4)
print(newlist)

# searching

print(list4.index(2))

# reverse

print(list4.reverse())

# count 

print(list4.count(2))



print(list1)
print(list2)
print(list3)
print(list4)


