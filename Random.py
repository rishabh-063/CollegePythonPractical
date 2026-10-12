import random

print(random.randint(1, 10))
print(random.uniform(1, 10))

list =[1,2,3,4,5,6,7,8,9]
print(random.choice(list))

string = "Hello, World!"
print(random.choice(string))


print(random.randrange(1, 10))
print(random.randrange(20,50,3))

# random.seed(5)
print(random.randint(1, 10))

# random.seed(7)
print(random.randint(1, 10))

random.shuffle(list)
print(list)