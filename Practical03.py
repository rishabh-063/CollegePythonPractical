# Create, write, append and read a text file.

with open("student.txt","w") as f:
    f.write("Asha,88\nRavi,91\n")
with open("student.txt","a") as f:
    f.write("Neha,87\n")
with open("student.txt","r") as f:
    print(f.read())