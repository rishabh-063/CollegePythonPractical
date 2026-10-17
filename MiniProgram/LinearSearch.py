def LinearSearch(list, key):
    for i in list:
        if key == i:
          return 1
    return 0

list =[21,3,5,23,10]
key =1
result = LinearSearch(list,key)
print("Present" if result==1 else "Absent")